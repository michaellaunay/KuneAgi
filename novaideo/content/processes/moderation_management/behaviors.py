# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

from pyramid.httpexceptions import HTTPFound

from dace.objectofcollaboration.principal.util import has_role
from dace.processinstance.activity import (
    ElementaryAction)


def decision_relation_validation(process, context):
    return process.execution_context.has_relation(context, 'content')


def decision_roles_validation(process, context):
    return has_role(role=('SiteAdmin',))


class ModerationVote(ElementaryAction):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'plus-action'
    style_order = 5
    processs_relation_id = 'content'
    #actionType = ActionType.system
    relation_validation = decision_relation_validation
    roles_validation = decision_roles_validation

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))
