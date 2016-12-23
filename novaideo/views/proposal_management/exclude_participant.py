# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

import deform
import colander
from pyramid.view import view_config

from substanced.util import get_oid

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.default_behavior import Cancel
from pontus.widget import Select2Widget
from pontus.form import FormView
from pontus.schema import Schema
from pontus.view import BasicView
from pontus.view_operation import MultipleView
from pontus.file import Object as ObjectType

from novaideo.content.processes.proposal_management.behaviors import (
    ExcludeParticipant)
from novaideo.content.proposal import Proposal
from novaideo import _


class ExcludeParticipantViewStudyReport(BasicView):
    title = _('Alert for exclusion')
    name = 'alertforexclusion'
    template = 'novaideo:views/proposal_management/templates/alert_exclusion.pt'

    def update(self):
        result = {}
        values = {'context': self.context}
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


@colander.deferred
def participant_choice(node, kw):
    context = node.bindings['context']
    in_process = [p.participant for p in context.ballot_processes
                  if p.id == 'exclusionparticipant']
    values = [(get_oid(m), m.title) for m in context.working_group.members
              if m not in in_process]
    values.insert(0, ('', _('- Select -')))
    return Select2Widget(
        values=values,
        multiple=False
        )


class ExclusionSchema(Schema):

    participant = colander.SchemaNode(
        ObjectType(),
        widget=participant_choice,
        missing=[],
        title=_("Participant to exclude")
        )


class ExcludeParticipantFormView(FormView):
    title = _('Participant exclusion')
    schema = ExclusionSchema()
    behaviors = [ExcludeParticipant, Cancel]
    formid = 'formexcludeparticipant'
    name = 'excludeparticipantform'

    def before_update(self):
        self.action = self.request.resource_url(
            self.context, 'novaideoapi',
            query={'op': 'update_action_view',
                   'node_id': ExcludeParticipant.node_definition.id})
        self.schema.widget = deform.widget.FormWidget(
            css_class='deform novaideo-ajax-form')


@view_config(
    name='excludeparticipant',
    context=Proposal,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class ExcludeParticipantView(MultipleView):
    title = _('Exclude participant from the working group')
    name = 'excludeparticipant'
    behaviors = [ExcludeParticipant]
    viewid = 'excludeparticipant'
    template = 'daceui:templates/simple_mergedmultipleview.pt'
    views = (ExcludeParticipantViewStudyReport, ExcludeParticipantFormView)
    validators = [ExcludeParticipant.get_validator()]


DEFAULTMAPPING_ACTIONS_VIEWS.update(
    {ExcludeParticipant: ExcludeParticipantView})
