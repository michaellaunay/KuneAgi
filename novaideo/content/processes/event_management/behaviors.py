# -*- coding: utf8 -*-
# Copyright (c) 2018 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

import datetime
import pytz
from persistent.list import PersistentList
from pyramid.httpexceptions import HTTPFound

from dace.objectofcollaboration.principal.util import (
    get_current,
    grant_roles,
    has_role,
    has_any_roles)
from dace.util import getSite
from dace.processinstance.activity import (
    InfiniteCardinality, ActionType)
from dace.processinstance.core import ActivityExecuted

from ..user_management.behaviors import (
    global_user_processsecurity,
    access_user_processsecurity)
from novaideo.content.interface import IEvent, IEventObject
from novaideo import _, nothing
from novaideo.core import access_action, serialize_roles
from novaideo.content.keyword import DEFAULT_TREE


def create_roles_validation(process, context):
    return has_role(role=('Member',))


def create_processsecurity_validation(process, context):
    user = get_current()
    current_events = [e for e in getattr(user, 'events', []) if not e.is_expired]
    nb_event_maxi = getattr(getSite(), 'nb_event_maxi', 7)
    return len(current_events) < nb_event_maxi and  global_user_processsecurity()


def create_state_validation(process, context):
    return 'published' in context.state


class Create(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-calendar'
    style_order = 0
    submission_title = _('Save')
    context = IEventObject
    roles_validation = create_roles_validation
    processsecurity_validation = create_processsecurity_validation
    state_validation = create_state_validation

    def start(self, context, request, appstruct, **kw):
        user = get_current(request)
        event = appstruct['_object_data']
        context.addtoproperty('events', event)
        event.state.append('published')
        event.tree = getattr(context, 'tree', DEFAULT_TREE)
        event.title = getattr(context, 'title', 'Discussion event')
        grant_roles(user=user, roles=(('Owner', event), ))
        event.setproperty('author', user)
        timezone = pytz.timezone(event.tzname)
        event.date = event.date.replace(tzinfo=timezone)
        event.init_published_at()
        event.format(request)
        event.reindex()
        return {'newcontext': event}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(kw['newcontext'], "@@index"))


def rm_roles_validation(process, context):
    return has_any_roles(roles=(('Owner', context), 'Moderator'))


def rm_processsecurity_validation(process, context):
    return global_user_processsecurity()


class Remove(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-trash'
    style_order = 6
    submission_title = _('Continue')
    context = IEvent
    roles_validation = rm_roles_validation
    processsecurity_validation = rm_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        context.subject.delfromproperty('events', context)
        return {}

    def redirect(self, context, request, **kw):
        root = getSite()
        return HTTPFound(request.resource_url(root))


def edit_roles_validation(process, context):
    return has_any_roles(roles=(('Owner', context), 'Moderator'))


def edit_processsecurity_validation(process, context):
    return global_user_processsecurity()


def edit_state_validation(process, context):
    return 'censored' not in context.state


class Edit(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'text-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-pencil'
    style_order = 1
    submission_title = _('Save')
    context = IEvent
    roles_validation = edit_roles_validation
    processsecurity_validation = edit_processsecurity_validation
    state_validation = edit_state_validation

    def start(self, context, request, appstruct, **kw):
        timezone = pytz.timezone(context.tzname)
        context.date = context.date.replace(tzinfo=timezone)
        context.state= PersistentList(['published'])
        context.update()
        context.format(request)
        context.reindex()
        request.registry.notify(ActivityExecuted(self, [context], get_current(request)))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def seeevents_state_validation(process, context):
    return 'published' in context.state


class SeeRelatedEvents(InfiniteCardinality):
    style_descriminator = 'plus-action'
    style_interaction = 'ajax-action'
    style_interaction_type = 'slider'
    style_picto = 'glyphicon glyphicon-calendar'
    style_order = 1
    context = IEventObject
    state_validation = seeevents_state_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def get_access_key(obj):
    if 'published' in obj.state:
        return ['always']
    else:
        return serialize_roles(
            (('Owner', obj), 'SiteAdmin', 'Admin', 'Moderator'))


def see_processsecurity_validation(process, context):
    return access_user_processsecurity(process, context) and \
           ('published' in context.state or 'censored' in context.state or\
            has_any_roles(roles=(('Owner', context), 'Moderator')))


@access_action(access_key=get_access_key)
class SeeEvent(InfiniteCardinality):
    """SeeEvent is the behavior allowing access to context"""
    style = 'button' #TODO add style abstract class
    style_descriminator = 'access-action'
    style_interaction = 'ajax-action'
    style_interaction_type = 'sidebar'
    style_picto = 'glyphicon glyphicon-eye-open'
    title = _('Details')
    context = IEvent
    actionType = ActionType.automatic
    processsecurity_validation = see_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        context.update()
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))

#TODO behaviors
