# -*- coding: utf8 -*-
# Copyright (c) 2016 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from pyramid.view import view_config

from substanced.util import Batch

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from dace.objectofcollaboration.principal.util import get_current
from pontus.view import BasicView

from novaideo.core import can_access, EventObject
from novaideo.content.processes.event_management.behaviors import (
    SeeRelatedEvents)
from novaideo.utilities.util import (
    render_small_listing_objs, render_listing_objs)
from novaideo import _

BATCH_DEFAULT_SIZE = 8

EVENTS_MESSAGES = {
    '0': _(u"""No organized event"""),
    '1': _(u"""One organized event"""),
    '*': _(u"""${number} organized events""")}


@view_config(
    name='relatedevents',
    context=EventObject,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class SeeRelatedEventsView(BasicView):
    name = 'relatedevents'
    viewid = 'relatedevents'
    behaviors = [SeeRelatedEvents]
    template = 'novaideo:views/novaideo_view_manager/templates/home.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    view_icon = 'glyphicon glyphicon-calendar'
    title = _('The related discussion events')
    description = _('See the related discussion events')

    def update(self):
        self.execute(None)
        user = get_current()
        objects = [event for event
                   in self.context.events
                   if 'published' in event.state and
                   can_access(user, event)]
        objects = sorted(
            objects,
            key=lambda e: getattr(e, 'modified_at'),
            reverse=True)
        is_small = True
        current_is_small = self.params('is_small')
        if current_is_small is not None:
            current_is_small = current_is_small.lower()
            is_small = current_is_small == 'true'
        elif self.parent or self.request.view_name == self.name:
            is_small = False

        url = self.request.resource_url(
            self.context, self.name, query={'is_small': str(is_small)})
        batch = Batch(objects, self.request,
                      url=url,
                      default_size=BATCH_DEFAULT_SIZE)
        batch.target = "#results_eventobject_events" + \
            str(self.context.__oid__) + \
            (is_small and 'is_small' or '')
        len_result = batch.seqlen
        index = str(len_result)
        if len_result > 1:
            index = '*'

        self.title = _(EVENTS_MESSAGES[index], mapping={'number': len_result})
        result = {}
        if is_small:
            result_body = render_small_listing_objs(
                self.request, batch, user)
        else:
            result_body, result = render_listing_objs(
                self.request, batch, user)

        values = {
            'bodies': result_body,
            'batch': batch,
            'empty_message': _("No organized event"),
            'empty_icon': 'glyphicon glyphicon-calendar'
        }
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


DEFAULTMAPPING_ACTIONS_VIEWS.update(
    {SeeRelatedEvents: SeeRelatedEventsView})
