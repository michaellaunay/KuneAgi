# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

import transaction
from pyramid.events import subscriber, ApplicationCreated
from pyramid.threadlocal import get_current_registry
from pyramid.request import Request
from pyramid.threadlocal import manager

from substanced.event import RootAdded
from substanced.util import find_service

from dace.util import getSite

from novaideo import core
from novaideo.utilities.util import send_alert_new_content
from novaideo.event import ObjectPublished, CorrelableRemoved


@subscriber(RootAdded)
def mysubscriber(event):
    """Add the novaideo catalog when the root is added."""
    root = event.object
    registry = get_current_registry()
    settings = registry.settings
    novaideo_title = settings.get('novaideo.title')
    root.title = novaideo_title
    catalogs = find_service(root, 'catalogs')
    catalogs.add_catalog('novaideo')
    ml_file = core.FileEntity(title="Legal notices")
    ml_file.__name__ = 'ml_file'
    root.addtoproperty('files', ml_file)
    root.ml_file = ml_file
    terms_of_use = core.FileEntity(title="Terms of use")
    terms_of_use.__name__ = 'terms_of_use'
    root.addtoproperty('files', terms_of_use)
    root.terms_of_use = terms_of_use


@subscriber(ObjectPublished)
def mysubscriber_object_published(event):
    published_object = event.object
    send_alert_new_content(published_object)


@subscriber(CorrelableRemoved)
def mysubscriber_correlable_removed(event):
    root = getSite()
    removed_object = event.object
    #get all versions. Versions will be removed
    all_versions = getattr(removed_object, 'history', [])
    if removed_object in all_versions:
        all_versions.remove(removed_object)

    #recuperate all correlations
    source_correlations = removed_object.source_correlations
    [source_correlations.extend(getattr(version, 'source_correlations', []))
     for version in all_versions]
    #destroy all versions
    if hasattr(removed_object, 'destroy'):
        removed_object.destroy()

    #update correlations
    for correlation in source_correlations:
        for target in list(correlation.targets):
            correlation.delfromproperty('targets', target)

        root.delfromproperty('correlations', correlation)


@subscriber(ApplicationCreated)
def init_application(event):
    app = event.object
    registry = app.registry
    request = Request.blank('/application_created') # path is meaningless
    request.registry = registry
    manager.push({'registry': registry, 'request': request})
    root = app.root_factory(request)
    request.root = root

    # other init functions
    init_contents(registry)

    transaction.commit()
    manager.pop()


def init_contents(registry):
    """Init searchable content"""
    core.SEARCHABLE_CONTENTS = {
        type_id: c
        for type_id, c in registry.content.content_types.items()
        if core.SearchableEntity in c.mro()
    }
