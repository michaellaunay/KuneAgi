# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

"""
This module represent all of behaviors used in the
FPTP election process definition.
"""
import datetime

from dace.util import getSite
from dace.processinstance.activity import InfiniteCardinality
from dace.objectofcollaboration.principal.util import get_current

from novaideo.content.interface import IProposal
from ..user_management.behaviors import global_user_processsecurity
from novaideo import _
from ..ballot_processes import Nothing


def note_relation_validation(process, context):
    return process.execution_context.has_relation(context, 'subject')


def note_processsecurity_validation(process, context):
    user = get_current()
    report = process.ballot.report
    elector = report.get_elector(user)
    return elector and not report.he_voted(elector) and \
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
        real_member = getattr(member, 'member', member)
        now = datetime.datetime.utcnow()
        real_member.add_note(
            user, context, note, now, getattr(root, 'time_constant', 6))
        real_member.reindex()
        ballot = self.process.ballot
        report = ballot.report
        elector = report.get_elector(user)
        report.addtoproperty('voters', elector)
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
        nothing = Nothing()
        nothing.is_nothing = True
        return nothing

#TODO behaviors
