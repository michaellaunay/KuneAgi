# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi
import datetime
from persistent.list import PersistentList
from pyramid.threadlocal import get_current_request

from dace.processdefinition.processdef import ProcessDefinition
from dace.processdefinition.activitydef import (
    SubProcessDefinition as OriginSubProcessDefinition)
from dace.processdefinition.transitiondef import TransitionDefinition
from dace.processdefinition.eventdef import (
    StartEventDefinition,
    EndEventDefinition)
from dace.processinstance.activity import (
    SubProcess as OriginSubProcess)
from dace.util import getSite
from pontus.core import VisualisableElement

from .behaviors import (
    StartBallot,
)
from novaideo import _
from novaideo.content.processes.ballot_processes import close_votes
from novaideo.content.ballot import Ballot
from . import get_ballot_data_by_type


class SubProcess(OriginSubProcess):

    def __init__(self, definition):
        super(SubProcess, self).__init__(definition)

    def stop(self):
        request = get_current_request()
        for process in self.sub_processes:
            exec_ctx = process.execution_context
            vote_processes = exec_ctx.get_involved_collection('vote_processes')
            vote_processes = [process for process in vote_processes
                              if not process._finished]
            if vote_processes:
                close_votes(None, request, vote_processes)

        super(SubProcess, self).stop()


class SubProcessDefinition(OriginSubProcessDefinition):
    """Run the voting process for the moderation of contents"""

    factory = SubProcess

    def _init_subprocess(self, process, subprocess):
        root = getSite()
        duration = datetime.timedelta(
            days=getattr(root, 'duration_moderation_vote', 7))
        execution_context = process.execution_context
        content = execution_context.created_entity(
            'content')
        electors = execution_context.get_involved_collection(
            'electors')
        subjects = [content]
        ballot_data = get_ballot_data_by_type(content, process.id)
        ballot = Ballot('Referendum', electors, subjects, duration,
                        true_val=ballot_data.get(
                            'true_value'),
                        false_val=ballot_data.get(
                            'false_value'))
        content.addtoproperty('ballots', ballot)
        ballot.report.description = ballot_data.get(
            'ballot_description', '')
        ballot.report.description_template = ballot_data.get(
            'ballot_description_template', None)
        title = ballot_data.get('ballot_title')
        if hasattr(title, '__call__'):
            title = title(process, content)

        ballot.title = title
        processes = ballot.run_ballot()
        subprocess.ballots = PersistentList()
        subprocess.ballots.append(ballot)
        subprocess.execution_context.add_involved_collection(
            'vote_processes', processes)
        subprocess.duration = duration


class ContentBallot(ProcessDefinition, VisualisableElement):
    isControlled = True
    isVolatile = True
    ballot_action = StartBallot

    def __init__(self, **kwargs):
        super(ContentBallot, self).__init__(**kwargs)
        self.title = _('Content ballot')
        self.description = _('Content ballot')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                start_ballot = SubProcessDefinition(pd='ballotprocess', contexts=[self.ballot_action],
                                       description=_("Start voting for ballot"),
                                       title=_("Start voting for ballot"),
                                       groups=[]),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'start_ballot'),
                TransitionDefinition('start_ballot', 'end'),
        )
