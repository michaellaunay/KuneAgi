# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

import deform
from pyramid.view import view_config

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.default_behavior import Cancel
from pontus.form import FormView
from pontus.schema import select

from novaideo.content.processes.event_management.behaviors import Edit
from novaideo.content.event import EventSchema, Event
from novaideo import _


@view_config(
    name='editevent',
    context=Event,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class EditEventView(FormView):

    title = _('Edit the discussion event')
    schema = select(EventSchema(factory=Event, editable=True),
                    ['kind',
                     'date',
                     'tzname',
                     'locale',
                     'text'])
    behaviors = [Edit, Cancel]
    formid = 'formeditevent'
    name = 'editevent'

    def before_update(self):
        self.action = self.request.resource_url(
            self.context, 'novaideoapi',
            query={'op': 'update_action_view',
                   'node_id': Edit.node_definition.id})
        self.schema.widget = deform.widget.FormWidget(
            css_class='deform novaideo-ajax-form')

    def default_data(self):
        return self.context


DEFAULTMAPPING_ACTIONS_VIEWS.update({Edit: EditEventView})
