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
from novaideo.content.question import Question
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
        self.title = _('Reported content management')
        self.description = _('Reported content management')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                pg = ParallelGatewayDefinition(),
                report = ActivityDefinition(contexts=[Report],
                                       description=_("Report the content"),
                                       title=_("Report"),
                                       groups=[]),
                see_reports = ActivityDefinition(contexts=[SeeReports],
                                       description=_("See reported contents"),
                                       title=_("Reported contents"),
                                       groups=[]),
                restor = ActivityDefinition(contexts=[Restor],
                                       description=_("Restore the content"),
                                       title=_("Restore the content"),
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


def question_title(process, context):
    return _("Vote to Moderate the reported question « ${content} »",
             mapping={'content': context.title})


QUESTION_MODERATION_GROUP = {
    'group_id': 'vote_moderation',
    'group_title': _('Moderate the question'),
    'group_activate': False,
    'group_activator_title': _('Moderate the question'),
    'group_activator_class_css': 'vote-action',
    'group_activator_style_picto': 'octicon octicon-check',
    'group_activator_order': 100
}


BALLOT_DATA[Question.__name__+'-contentreportdecision'] = {
    'ballot_description_template': 'novaideo:views/templates/ballots/question_report.pt',
    'ballot_title': question_title,
    'true_value': _("This question complies with the Moderation Charter"),
    'false_value': _("This question DOES NOT comply with the Moderation Charter"),
    'process_id': 'contentreportdecision',
    'group': QUESTION_MODERATION_GROUP
}


def idea_title(process, context):
    return _("Vote to Moderate the reported idea « ${content} »",
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
    'true_value': _("This idea complies with the Moderation Charter"),
    'false_value': _("This idea DOES NOT comply with the Moderation Charter"),
    'process_id': 'contentreportdecision',
    'group': IDEA_MODERATION_GROUP
}


def proposal_title(process, context):
    return _("Vote to Moderate the reported Proposal « ${content} »",
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
    'true_value': _("This Proposal complies with the Moderation Charter"),
    'false_value': _("This Proposal DOES NOT comply with the Moderation Charter"),
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
    'ballot_title': _("Vote to Moderate the reported comment"),
    'true_value': _("This comment complies with the Moderation Charter"),
    'false_value': _("This comment DOES NOT comply with the Moderation Charter"),
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
