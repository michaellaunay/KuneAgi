# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from dace.util import getSite
from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from dace.objectofcollaboration.principal.util import (
    get_current, has_any_roles)
from pontus.view import BasicView
from pontus.view_operation import MultipleView
from pontus.util import merge_dicts

from novaideo.content.processes.idea_management.behaviors import SeeIdea
from novaideo.content.idea import Idea
from novaideo.content.processes import get_states_mapping
from novaideo.utilities.util import (
    generate_navbars, ObjectRemovedException,
    get_vote_actions_body)
from novaideo import _
from .compare_idea import CompareIdeaView
from .see_workinggroups import SeeRelatedWorkingGroupsView
from ..event_management.see_events import SeeRelatedEventsView


class IdeaHeaderView(BasicView):
    name = 'ideaheader'
    viewid = 'ideaheader'
    behaviors = [SeeIdea]
    validate_behaviors = False
    template = 'novaideo:views/idea_management/templates/header_idea.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    requirements = {'css_links': [],
                    'js_links': ['novaideo:static/js/ballot_management.js']}
    title = _('Idea header')

    def _cant_publish_alert(self, actions, user):
        if not self.request.moderate_ideas and \
           'to work' in self.context.state and self.context.author is user:
            return not any(a.behavior_id == 'publish'
                           for a in actions.get('global-action', []))

        return False

    def _cant_submit_alert(self, actions, user):
        if self.request.moderate_ideas and \
           'to work' in self.context.state and self.context.author is user:
            return not any(a.behavior_id == 'submit'
                           for a in actions.get('global-action', []))

        return False

    def update(self):
        vote_actions = self.get_binding('vote_actions')
        navbars = self.get_binding('navbars')
        root = self.get_binding('root')
        if navbars is None:
            return HTTPFound(self.request.resource_url(root, ''))

        resources = merge_dicts(navbars['resources'], vote_actions['resources'],
                                ('js_links', 'css_links'))
        resources['js_links'] = list(set(resources['js_links']))
        resources['css_links'] = list(set(resources['css_links']))
        messages = vote_actions['messages']
        if not messages:
            messages = navbars['messages']

        user = self.get_binding('user')
        is_censored = self.get_binding('is_censored')
        to_hide = self.get_binding('to_hide')
        result = {}
        values = {
            'idea': self.context,
            'is_censored': is_censored,
            'to_hide': to_hide,
            'state': get_states_mapping(
                user, self.context, self.context.state[0]),
            'current_user': user,
            'cant_publish': self._cant_publish_alert(
                navbars['all_actions'], user),
            'cant_submit': self._cant_submit_alert(
                navbars['all_actions'], user),
            'navbar_body': navbars['navbar_body'],
            'vote_actions_body': vote_actions['body']
        }
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        item['messages'] = messages
        item['isactive'] = vote_actions['isactive'] or navbars['isactive']
        result.update(resources)
        result['coordinates'] = {self.coordinates: [item]}
        return result


class DetailIdeaView(BasicView):
    name = 'seeIdea'
    viewid = 'seeidea'
    behaviors = [SeeIdea]
    validate_behaviors = False
    view_icon = 'glyphicon glyphicon-eye-open'
    template = 'novaideo:views/idea_management/templates/see_idea.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    title = _('Details')

    def update(self):
        self.execute(None)
        navbars = self.get_binding('navbars')
        root = self.get_binding('root')
        if navbars is None:
            return HTTPFound(self.request.resource_url(root, ''))

        user = self.get_binding('user')
        to_hide = self.get_binding('to_hide')
        result = {}
        values = {
            'idea': self.context,
            'to_hide': to_hide,
            'text': self.context.text.replace('\n', '<br/>'),
            'current_user': user,
            'footer_body': navbars['footer_body']
        }
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        item['isactive'] = True
        result['coordinates'] = {self.coordinates: [item]}
        result = merge_dicts(self.requirements_copy, result)
        return result


class SeeIdeaActionsView(MultipleView):
    name = 'seeiactionsdea'
    template = 'novaideo:views/templates/multipleview.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    css_class = 'integreted-tab-content'
    title = ''
    views = (DetailIdeaView, SeeRelatedWorkingGroupsView, SeeRelatedEventsView, CompareIdeaView,)

    def _activate(self, items):
        pass


@view_config(
    name='seeidea',
    context=Idea,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class SeeIdeaView(MultipleView):
    name = 'seeidea'
    template = 'novaideo:views/templates/entity_multipleview.pt'
    title = ''
    views = (IdeaHeaderView, SeeIdeaActionsView)
    requirements = {'css_links': [],
                    'js_links': ['novaideo:static/js/compare_idea.js',
                                 'novaideo:static/js/comment.js',
                                 'novaideo:static/js/ballot_management.js']}
    validators = [SeeIdea.get_validator()]

    def bind(self):
        bindings = {}
        bindings['navbars'] = None
        bindings['vote_actions'] = None
        vote_actions = get_vote_actions_body(
            self.context, self.request)
        try:
            navbars = generate_navbars(
                self.request, self.context,
                text_action=vote_actions['activators'])
            bindings['navbars'] = navbars
            bindings['vote_actions'] = vote_actions
        except ObjectRemovedException:
            return

        bindings['user'] = get_current()
        bindings['root'] = getSite()
        bindings['is_censored'] = 'censored' in self.context.state
        bindings['to_hide'] = bindings['is_censored'] and not has_any_roles(
            user=bindings['user'],
            roles=(('Owner', self.context), 'Moderator'))
        setattr(self, '_bindings', bindings)


DEFAULTMAPPING_ACTIONS_VIEWS.update(
    {SeeIdea: SeeIdeaView})
