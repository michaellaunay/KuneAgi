# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.view import BasicView

from novaideo.content.processes.user_management.behaviors import  ConfirmQuitRequest
from novaideo.content.person import QuitRequest
from novaideo.content.novaideo_application import NovaIdeoApplication
from novaideo import _

@view_config(
    name='',
    context=QuitRequest,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class ConfirmQuitRequestView(BasicView):
    title = _('Confirm the resignation request')
    name = ''
    behaviors = [ConfirmQuitRequest]
    viewid = 'resignationconfirmation'

    def update(self):
        self.execute(None)
        headers = forget(self.request)
        return HTTPFound(
            location=self.request.resource_url(
                self.request.root, '@@resignationconfirmed'),
            headers=headers)


@view_config(
    name='resignationconfirmed',
    context=NovaIdeoApplication,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class ConfirmedQuitRequestView(BasicView):
    template = 'novaideo:views/user_management/templates/resignationconfirmed.pt'
    title = _('Resignation confirmed')
    name = 'resignationconfirmed'
    viewid = 'resignationconfirmed'
    css_class = 'panel-transparent'

    def update(self):
        result = {}
        body = self.content(args={}, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


DEFAULTMAPPING_ACTIONS_VIEWS.update({ConfirmQuitRequest:ConfirmQuitRequestView})