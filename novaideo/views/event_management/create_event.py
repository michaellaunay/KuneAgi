# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

import deform
from pyramid.view import view_config

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.default_behavior import Cancel
from pontus.form import FormView
from pontus.schema import select, omit

from novaideo.content.processes.event_management.behaviors import (
    Create)
from novaideo.content.event import EventSchema, Event
from novaideo.core import EventObject
from novaideo import _, log


@view_config(
    name='createevent',
    context=EventObject,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class CreateEventView(FormView):

    title = _('Organize a discussion event')
    schema = omit(select(EventSchema(factory=Event, editable=True),
                    ['kind',
                     'date',
                     'tzname',
                     'locale',
                     'text']),
                  ["_csrf_token_"])
    behaviors = [Create, Cancel]
    formid = 'formcreateevent'
    name = 'createevent'
    css_class = 'panel-transparent'

    def before_update(self):
        self.action = self.request.resource_url(
            self.context, 'novaideoapi',
            query={'op': 'update_action_view',
                   'node_id': Create.node_definition.id})
        self.schema.widget = deform.widget.FormWidget(
            css_class='deform novaideo-ajax-form')


DEFAULTMAPPING_ACTIONS_VIEWS.update(
    {Create: CreateEventView})
