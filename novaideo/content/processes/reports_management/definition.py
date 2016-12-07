# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

from dace.processdefinition.processdef import ProcessDefinition
from dace.processdefinition.activitydef import ActivityDefinition
from dace.processdefinition.gatewaydef import (
    ExclusiveGatewayDefinition,
    ParallelGatewayDefinition)
from dace.processdefinition.transitiondef import TransitionDefinition
from dace.processdefinition.eventdef import (
    StartEventDefinition,
    EndEventDefinition)
from dace.objectofcollaboration.services.processdef_container import (
    process_definition)
from pontus.core import VisualisableElement

from .behaviors import (
    Report,
    Restor,
    SeeReports,
    ModerationVote)
from novaideo import _
from novaideo.content.proposal import Proposal
from novaideo.content.idea import Idea
from novaideo.content.comment import Comment
from novaideo.content.processes.content_ballot_management import (
    BALLOT_DATA)
from novaideo.content.processes.content_ballot_management.definition import (
    ContentBallot)


@process_definition(name='reportsmanagement', id='reportsmanagement')
class ReportsManagementProcess(ProcessDefinition, VisualisableElement):
    isUnique = True

    def __init__(self, **kwargs):
        super(ReportsManagementProcess, self).__init__(**kwargs)
        self.title = _('Reports management')
        self.description = _('Reports management')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                pg = ParallelGatewayDefinition(),
                report = ActivityDefinition(contexts=[Report],
                                       description=_("Report the content"),
                                       title=_("Report"),
                                       groups=[]),
                see_reports = ActivityDefinition(contexts=[SeeReports],
                                       description=_("See reports"),
                                       title=_("Reports"),
                                       groups=[]),
                restor = ActivityDefinition(contexts=[Restor],
                                       description=_("Restor the content"),
                                       title=_("Restor the content"),
                                       groups=[]),
                eg = ExclusiveGatewayDefinition(),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'pg'),
                TransitionDefinition('pg', 'report'),
                TransitionDefinition('report', 'eg'),
                TransitionDefinition('pg', 'see_reports'),
                TransitionDefinition('see_reports', 'eg'),
                TransitionDefinition('pg', 'restor'),
                TransitionDefinition('restor', 'eg'),
                TransitionDefinition('eg', 'end'),

        )


MODERATION_DESCRIPTION = _("Vous êtes invité à vérifier et modérer le contenu signalé. "
                           "Cela afin de garantir le respect de la charte d'utilisation. "
                           "Si la majorité vote en faveur du contenu, "
                           "les signalisations seront ignorées, sinon le contenu sera censuré.")


def content_title(process, context):
    return _("Moderation of ${content}",
             mapping={'content': context.title})


BALLOT_DATA[Idea.__name__+'-contentreportdecision'] = {
    'ballot_description': MODERATION_DESCRIPTION,
    'ballot_title': content_title,
    'true_value': _("Ignore"),
    'false_value': _("Censor"),
    'process_id': 'contentreportdecision'
}

BALLOT_DATA[Proposal.__name__+'-contentreportdecision'] = {
    'ballot_description': MODERATION_DESCRIPTION,
    'ballot_title': content_title,
    'true_value': _("Ignore"),
    'false_value': _("Censor"),
    'process_id': 'contentreportdecision'
}

BALLOT_DATA[Comment.__name__+'-contentreportdecision'] = {
    'ballot_description': MODERATION_DESCRIPTION,
    'ballot_title': _("Moderation of a comment"),
    'true_value': _("Ignore"),
    'false_value': _("Censor"),
    'process_id': 'contentreportdecision'
}


@process_definition(
    name='contentreportdecision',
    id='contentreportdecision')
class ReportingProcess(ContentBallot):
    ballot_action = ModerationVote

    def __init__(self, **kwargs):
        super(ReportingProcess, self).__init__(**kwargs)
