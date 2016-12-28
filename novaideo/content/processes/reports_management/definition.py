# -*- coding: utf8 -*-
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


def idea_title(process, context):
    return _("Vote de Modération sur l'idée signalée « ${content} »",
             mapping={'content': context.title})


IDEA_MODERATION_GROUP = {
    'group_id': 'vote_moderation',
    'group_title': _('Moderate the idea'),
    'group_activate': False,
    'group_activator_title': _('Moderate the idea'),
    'group_activator_class_css': 'vote-action',
    'group_activator_style_picto': 'octicon octicon-check',
    'group_activator_order': 100
}


BALLOT_DATA[Idea.__name__+'-contentreportdecision'] = {
    'ballot_description_template': 'novaideo:views/templates/ballots/idea_report.pt',
    'ballot_title': idea_title,
    'true_value': _("Cette idée est conforme à la Charte de Modération"),
    'false_value': _("Cette idée n'est pas conforme à la Charte de Modération"),
    'process_id': 'contentreportdecision',
    'group': IDEA_MODERATION_GROUP
}


def proposal_title(process, context):
    return _("Vote de Modération sur la proposition signalée « ${content} »",
             mapping={'content': context.title})


PROPOSAL_MODERATION_GROUP = {
    'group_id': 'vote_moderation',
    'group_title': _('Moderate the proposal'),
    'group_activate': False,
    'group_activator_title': _('Moderate the proposal'),
    'group_activator_class_css': 'vote-action',
    'group_activator_style_picto': 'octicon octicon-check',
    'group_activator_order': 100
}


BALLOT_DATA[Proposal.__name__+'-contentreportdecision'] = {
    'ballot_description_template': 'novaideo:views/templates/ballots/proposal_report.pt',
    'ballot_title': proposal_title,
    'true_value': _("Cette proposition est conforme à la Charte de Modération"),
    'false_value': _("Cette proposition n'est pas conforme à la Charte de Modération"),
    'process_id': 'contentreportdecision',
    'group': PROPOSAL_MODERATION_GROUP
}


COMMENT_MODERATION_GROUP = {
    'group_id': 'vote_moderation',
    'group_title': _('Moderate the comment'),
    'group_activate': False,
    'group_activator_title': _('Moderate the comment'),
    'group_activator_class_css': 'vote-action',
    'group_activator_style_picto': 'octicon octicon-check',
    'group_activator_order': 100
}


BALLOT_DATA[Comment.__name__+'-contentreportdecision'] = {
    'ballot_description_template': 'novaideo:views/templates/ballots/comment_report.pt',
    'ballot_title': _("Vote de Modération sur un commentaire signalé"),
    'true_value': _("Ce commentaire est conforme à la Charte de Modération"),
    'false_value': _("Ce commentaire n'est pas conforme à la Charte de Modération"),
    'process_id': 'contentreportdecision',
    'group': COMMENT_MODERATION_GROUP
}


@process_definition(
    name='contentreportdecision',
    id='contentreportdecision')
class ReportingProcess(ContentBallot):
    ballot_action = ModerationVote

    def __init__(self, **kwargs):
        super(ReportingProcess, self).__init__(**kwargs)
