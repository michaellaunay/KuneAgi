# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

"""
This module represent all of behaviors used in the
FPTP election process definition.
"""
from pyramid.httpexceptions import HTTPFound

from dace.util import getSite
from dace.processinstance.activity import InfiniteCardinality
from dace.objectofcollaboration.principal.util import get_current

from novaideo.content.interface import IProposal
from ..user_management.behaviors import global_user_processsecurity
from novaideo import _


def note_relation_validation(process, context):
    return process.execution_context.has_relation(context, 'subject')


def note_processsecurity_validation(process, context):
    user = get_current()
    report = process.ballot.report
    return user in report.electors and \
        user not in report.voters and \
        global_user_processsecurity()


class Note(InfiniteCardinality):
    title = _('Note')
    submission_title = _('Save')
    access_controled = True
    context = IProposal
    processs_relation_id = 'subject'
    relation_validation = note_relation_validation
    processsecurity_validation = note_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        note = appstruct['note']
        user = get_current()
        root = getSite()
        member = self.process.execution_context.involved_entity('member')
        member.set_confidence_index(
            user, note, getattr(root, 'time_constant', 6))
        ballot = self.process.ballot
        report = ballot.report
        report.addtoproperty('voters', user)
        return {}

    def after_execution(self, context, request, **kw):
        if self.isSequential:
            self.unlock(request)
            self.workitem.unlock(request)

        report = self.process.ballot.report
        if len(report.electors) == len(report.voters):
            self.isexecuted = True
            self.workitem.node.finish_behavior(self.workitem)

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, '@@index'))

#TODO behaviors
