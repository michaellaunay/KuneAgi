# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from dace.util import getSite
from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.view import BasicView
from pontus.util import merge_dicts

from novaideo.content.processes.user_management.behaviors import (
    SeeRegistration)
from novaideo.content.person import Preregistration
from novaideo.utilities.util import (
    generate_navbars,
    ObjectRemovedException,
    get_vote_actions_body)
from novaideo import _


@view_config(
    name='seeregistration',
    context=Preregistration,
    renderer='pontus:templates/views_templates/grid.pt',
)
class SeeRegistrationView(BasicView):
    title = ''
    name = 'seeregistration'
    behaviors = [SeeRegistration]
    template = 'novaideo:views/user_management/templates/see_registration.pt'
    viewid = 'seeregistration'
    requirements = {'css_links': [],
                    'js_links': ['novaideo:static/js/ballot_management.js']}

    def update(self):
        self.execute(None)
        vote_actions = get_vote_actions_body(
            self.context, self.request)
        try:
            navbars = generate_navbars(
                self.request, self.context,
                text_action=vote_actions['activators'])
        except ObjectRemovedException:
            return HTTPFound(self.request.resource_url(getSite(), ''))

        resources = merge_dicts(navbars['resources'], vote_actions['resources'],
                                ('js_links', 'css_links'))
        resources['js_links'] = list(set(resources['js_links']))
        resources['css_links'] = list(set(resources['css_links']))
        messages = vote_actions['messages']
        if not messages:
            messages = navbars['messages']

        values = {'registration': self.context,
                  'footer_body': navbars['footer_body'],
                  'navbar_body': navbars['navbar_body'],
                  'vote_actions_body': vote_actions['body']}
        result = {}
        body = self.content(
            args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        item['messages'] = messages
        item['isactive'] = vote_actions['isactive'] or navbars['isactive']
        result.update(resources)
        result['coordinates'] = {self.coordinates: [item]}
        result = merge_dicts(self.requirements_copy, result)
        return result


DEFAULTMAPPING_ACTIONS_VIEWS.update({SeeRegistration: SeeRegistrationView})
