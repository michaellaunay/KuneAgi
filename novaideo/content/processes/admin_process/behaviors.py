# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from io import StringIO, BytesIO
import csv
import pytz
import datetime
from persistent.list import PersistentList
from pyramid.httpexceptions import HTTPFound
from pyramid.response import FileIter

from dace.util import getSite
from dace.objectofcollaboration.principal.util import (
    has_any_roles,
    get_current,
    grant_roles,
    has_role)
from dace.processinstance.activity import (
    InfiniteCardinality,
    ActionType)
from deform_treepy.utilities.tree_utility import edit_keywords

from novaideo.adapters import (
    IExtractionAdapter, EXTRACTION_ATTR)
from novaideo.utilities.util import to_localized_time
from novaideo.content.interface import (
    INovaIdeoApplication,
    ISearchableEntity,
    ISmartFolder)
from novaideo import _, nothing
from novaideo.views.filter import find_entities
from novaideo.core import access_action, serialize_roles


def siteadmin_roles_validation(process, context):
    return has_any_roles(roles=('SiteAdmin', ))


class ConfigureSite(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'admin-action'
    style_picto = 'glyphicon glyphicon-wrench'
    style_order = 0
    submission_title = _('Save')
    context = INovaIdeoApplication
    roles_validation = siteadmin_roles_validation

    def start(self, context, request, appstruct, **kw):
        site = appstruct['_object_data']
        # work_conf = appstruct.pop('work_conf')
        # site.set_data(work_conf)
        site.modified_at = datetime.datetime.now(tz=pytz.UTC)
        # deadline = work_conf.pop('deadline', None)
        # if deadline:
        #     deadline = deadline.replace(tzinfo=pytz.UTC)
        #     if site.deadlines:
        #         current = site.deadlines[-1]
        #         site.deadlines.remove(current)

        #     site.deadlines.append(deadline)

        site.reindex()
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, ""))


class ManageKeywords(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'admin-action'
    style_picto = 'glyphicon glyphicon-tags'
    style_order = 8
    submission_title = _('Save')
    context = INovaIdeoApplication
    processsecurity_validation = siteadmin_roles_validation

    def start(self, context, request, appstruct, **kw):
        source = appstruct['source']
        targets = appstruct['targets']
        root = getSite()
        edited = edit_keywords(targets, source, root.tree)
        if edited:
            root.tree = edited

        objects = find_entities(interfaces=[ISearchableEntity],
                                keywords=[kw.lower() for kw in targets])
        for obj in objects:
            edited = edit_keywords(targets, source, obj.tree)
            if edited:
                obj.tree = edited
                obj.reindex()

        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, ""))


class Extract(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'admin-action'
    style_picto = 'glyphicon glyphicon-export'
    style_order = 8
    submission_title = _('Continue')
    context = INovaIdeoApplication
    processsecurity_validation = siteadmin_roles_validation

    def start(self, context, request, appstruct, **kw):
        user = get_current()
        localizer = request.localizer
        appstruct.pop('_csrf_token_')
        attributes_to_extract = appstruct.pop('attributes_to_extract')
        if not attributes_to_extract:
            attributes_to_extract = list(EXTRACTION_ATTR.keys())

        attributes_to_extract = sorted(
            attributes_to_extract, key=lambda a: EXTRACTION_ATTR[a]['order'])
        objects = find_entities(
            user=user,
            sort_on='release_date',
            **appstruct
        )
        csv_file = StringIO()
        fieldnames = []
        for attr in attributes_to_extract:
            fieldnames.append(
                localizer.translate(EXTRACTION_ATTR[attr]['title']))

        writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, dialect='excel', delimiter=';')
        writer.writeheader()
        registry = request.registry
        for obj in objects:
            adapter = registry.queryAdapter(
                obj, IExtractionAdapter)
            if adapter:
                writer.writerow(
                    dict([(localizer.translate(EXTRACTION_ATTR[attr]['title']),
                           localizer.translate(getattr(adapter, attr)(
                               user, request))) for
                          attr in attributes_to_extract]))

        csv_file.seek(0)
        return {'file': BytesIO(csv_file.read().encode('windows-1252', 'replace')),
                'filter': appstruct, 'user': user}

    def redirect(self, context, request, **kw):
        filter_ = kw.get('filter', None)
        keywords = []
        if filter_:
            keywords = list(filter_.get(
                'metadata_filter', {}).get(
                'keywords', []))

        keywords = '-'.join(keywords)
        user = kw.get('user', None)
        user_title = getattr(user, 'title', user.name)
        now = datetime.datetime.now()
        date = to_localized_time(now, request=request, translate=True)
        file_name = 'Extraction_{keywords}_{date}_{user}'.format(
            keywords=keywords, date=date, user=user_title)
        file_name = file_name.replace(' ', '-')
        csv_file = kw.get('file', '')
        response = request.response
        response.content_type = 'application/vnd.ms-excel;charset=windows-1252'
        response.content_disposition = 'inline; filename="{file_name}.csv"'.format(
            file_name=file_name)
        response.app_iter = FileIter(csv_file)
        return response

# Smart folders


def get_access_key(obj):
    if 'published' in obj.state:
        return ['always']
    else:
        return serialize_roles((('Owner', obj), 'SiteAdmin', 'Admin'))


def see_processsecurity_validation(process, context):
    return 'published' in context.state or \
           has_any_roles(roles=('SiteAdmin', 'Admin'))\
           or has_role(role=('Owner', context))


@access_action(access_key=get_access_key)
class SeeSmartFolder(InfiniteCardinality):
    """SeeFile is the behavior allowing access to context"""
    title = _('Details')
    context = ISmartFolder
    actionType = ActionType.automatic
    processsecurity_validation = see_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def create_roles_validation(process, context):
    return has_role(role=('Member',))


class AddSmartFolder(InfiniteCardinality):
    style_descriminator = 'admin-action'
    style_picto = 'glyphicon glyphicon-folder-open'
    style_order = 0
    submission_title = _('Save')
    context = INovaIdeoApplication
    roles_validation = create_roles_validation

    def start(self, context, request, appstruct, **kw):
        new_smart_folder = appstruct['_object_data']
        context.addtoproperty('smart_folders', new_smart_folder)
        grant_roles(roles=(('Owner', new_smart_folder), ))
        new_smart_folder.setproperty('author', get_current())
        new_smart_folder.state = PersistentList(['private'])
        new_smart_folder.reindex()
        return {'newcontext': new_smart_folder}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(kw['newcontext'], "@@index"))


def createsub_roles_validation(process, context):
    return has_any_roles(roles=('SiteAdmin', 'Admin'))\
           or has_role(role=('Owner', context))


class AddSubSmartFolder(InfiniteCardinality):
    style_descriminator = 'admin-action'
    style_picto = 'glyphicon glyphicon-folder-open'
    style_interaction = 'ajax-action'
    style_order = 0
    submission_title = _('Save')
    context = ISmartFolder
    roles_validation = createsub_roles_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        new_smart_folder = appstruct['_object_data']
        root.addtoproperty('smart_folders', new_smart_folder)
        context.addtoproperty('children', new_smart_folder)
        grant_roles(roles=(('Owner', new_smart_folder), ))
        new_smart_folder.setproperty('author', get_current())
        new_smart_folder.state = PersistentList(['private'])
        new_smart_folder.filters = PersistentList(
            getattr(new_smart_folder, 'filters', []))
        new_smart_folder.reindex()
        return {'newcontext': new_smart_folder}

    def redirect(self, context, request, **kw):
        return nothing


def edit_roles_validation(process, context):
    return has_any_roles(roles=('SiteAdmin', 'Admin')) or \
        has_role(role=('Owner', context))


def edit_state_validation(process, context):
    return 'private' in context.state or \
        has_any_roles(roles=('SiteAdmin', 'Admin'))


class EditSmartFolder(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'text-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-pencil'
    style_order = 1
    submission_title = _('Save')
    context = ISmartFolder
    roles_validation = edit_roles_validation
    state_validation = edit_state_validation

    def start(self, context, request, appstruct, **kw):
        context.filters = PersistentList(getattr(context, 'filters', []))
        context.modified_at = datetime.datetime.now(tz=pytz.UTC)
        context.reindex()
        return {}

    def redirect(self, context, request, **kw):
        return nothing


class RemoveSmartFolder(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-trash'
    style_order = 2
    submission_title = _('Continue')
    context = ISmartFolder
    roles_validation = edit_roles_validation
    state_validation = edit_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        sub_folders = context.all_sub_folders()
        for sub_folder in sub_folders:
            root.delfromproperty('smart_folders', sub_folder)

        root.delfromproperty('smart_folders', context)
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def admin_roles_validation(process, context):
    return has_role(role=('Admin',))


def siteadmin_roles_validation(process, context):
    return has_any_roles(roles=('SiteAdmin', 'Admin'))


def pub_state_validation(process, context):
    return 'private' in context.state


class PublishSmartFolder(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-share'
    style_order = 2
    submission_title = _('Continue')
    context = ISmartFolder
    roles_validation = siteadmin_roles_validation
    state_validation = pub_state_validation

    def start(self, context, request, appstruct, **kw):
        context.state = PersistentList(['published'])
        context.reindex()
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def withdraw_processsecurity_validation(process, context):
    return 'published' in context.state


class WithdrawSmartFolder(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-fast-backward'
    style_order = 2
    submission_title = _('Continue')
    context = ISmartFolder
    roles_validation = siteadmin_roles_validation
    processsecurity_validation = withdraw_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        context.state = PersistentList(['private'])
        context.reindex()
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def seesmartfolders_roles_validation(process, context):
    return has_role(role=('Member',))


class SeeSmartFolders(InfiniteCardinality):
    style_descriminator = 'admin-action'
    style_picto = 'glyphicon glyphicon-folder-open'
    style_order = 2
    context = INovaIdeoApplication
    roles_validation = seesmartfolders_roles_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context))


def order_processsecurity_validation(process, context):
    return len(context.smart_folders) > 1 and has_any_roles(roles=('SiteAdmin', 'Admin'))


class OrderSmartFolders(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'body-action'
    style_picto = 'glyphicon glyphicon-th-list'
    style_order = 8
    template = 'novaideo:views/templates/order_smart_folders.pt'
    submission_title = _('Save')
    context = INovaIdeoApplication
    processsecurity_validation = order_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        folders = appstruct['folders']
        for index, folder in enumerate(folders):
            folder.set_order(index)

        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@seesmartfolders"))


def ordersub_processsecurity_validation(process, context):
    return len(context.children) > 1 and has_any_roles(roles=('SiteAdmin', 'Admin'))


class OrderSubSmartFolders(OrderSmartFolders):
    context = ISmartFolder
    processsecurity_validation = ordersub_processsecurity_validation

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))

#TODO behaviors
