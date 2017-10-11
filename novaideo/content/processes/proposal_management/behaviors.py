# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

"""
This module represent all of behaviors used in the 
Proposal management process definition. 
"""
import datetime
import pytz
from persistent.list import PersistentList
from persistent.dict import PersistentDict
from pyramid.httpexceptions import HTTPFound
from pyramid.threadlocal import get_current_request

from substanced.util import get_oid

from dace.util import (
    getSite,
    copy,
    find_service)
from dace.objectofcollaboration.principal.util import (
    has_role,
    grant_roles,
    get_current,
    revoke_roles,
    has_any_roles)
#from dace.objectofcollaboration import system
import html_diff_wrapper
from dace.processinstance.activity import (
    InfiniteCardinality, ElementaryAction, ActionType)
from dace.processinstance.core import ActivityExecuted
from pontus.file import OBJECT_DATA
from pontus.interfaces import IFile

from novaideo.content.interface import (
    INovaIdeoApplication,
    IProposal,
    Iidea,
    IWorkspace)
from ..user_management.behaviors import (
    global_user_processsecurity,
    access_user_processsecurity)
from novaideo import _, nothing
from novaideo.content.proposal import Proposal
from ..comment_management import VALIDATOR_BY_CONTEXT
from novaideo.content.correlation import CorrelationType
from novaideo.content.working_group import WorkingGroup
from novaideo.content.processes.idea_management.behaviors import (
    PresentIdea,
    CommentIdea,
    Associate as AssociateIdea)
from novaideo.utilities.util import (
    connect, to_localized_time)
from novaideo.event import (
    ObjectPublished, CorrelableRemoved)
from novaideo.content.processes.proposal_management import WORK_MODES
from novaideo.core import access_action, serialize_roles, Evaluations
from novaideo.content.alert import InternalAlertKind
from novaideo.content.workspace import Workspace
from novaideo.views.filter import (
    get_users_by_preferences, get_random_users)
from novaideo.utilities.alerts_utility import (
    alert, get_user_data, get_entity_data, alert_comment_nia)
from . import (
    AMENDMENTS_CYCLE_DEFAULT_DURATION,
    init_proposal_ballots,
    add_files_to_workspace,
    add_attached_files)
from novaideo.content.processes.ballot_processes import close_votes
from . import end_work, remove_participant_from_ballots
from novaideo.content.processes.content_ballot_management import (
    ballot_result, close_ballot,
    ELECTORS_NB, start_ballot, remove_ballot_processes,
    get_ballot_alert_data)
from novaideo.content.processes.content_ballot_management.behaviors import (
    StartBallot)
from novaideo.content.processes.member_notation_management import (
    run_notation_process)


VOTE_PUBLISHING_MESSAGE = _("Each participant in the working group votes for or against continuing the improvement of the proposal. "
                            "If the majority is \"In favour\", a new improvement cycle begins. "
                            "If not, the proposal is submitted as is to the evaluation of the other "
                            "members of the platform.")


VOTE_DURATION_MESSAGE = _("Voting results regarding the further improvement of the proposal will not be known until the end of the ballot. "
                          "If the majority happens to vote for continuing to improve the "
                          "proposal, your vote on the duration of the improvement cycle is needed.")

VOTE_MODEWORK_MESSAGE = _("Voting results regarding the further improvement of the proposal will not be known until the end of the ballot. "
                          "If the majority happens to vote for continuing to improve the "
                          "proposal before submitting it to the other members of the platform,"
                          " your vote on the operating method of the working group is needed.")


VOTE_REOPENING_MESSAGE = _("Voting results regarding the further improvement of the proposal will not be known until the end of the ballot. "
                           "If the majority happens to vote for continuing to improve the "
                           "proposal before submitting it to the other members of the platform,"
                          " your vote on reopening the working group is needed.")


_marker = object()


def confirm_proposal(
    context, request, user, submitted_appstruct, root):
    working_group = context.working_group
    if context.originalentity:
        # Add Nia comment
        alert_comment_nia(
            context.originalentity, request, root,
            internal_kind=InternalAlertKind.content_alert,
            subject_type='proposal',
            alert_kind='duplicated',
            duplication=context
            )
    
    proposal_state = 'amendable'
    if submitted_appstruct.get('vote', False):
        proposal_state = 'published'
        if root.support_proposals:
            proposal_state = 'submitted_support'
            context.state = PersistentList(
                ['submitted_support', 'published'])
            # Add Nia comment
            alert_comment_nia(
                context, request, root,
                internal_kind=InternalAlertKind.working_group_alert,
                subject_type='proposal',
                alert_kind='submitted_support',
                duplication=context
                )
        else:
            context.state = PersistentList(
                ['published', 'submitted_support'])

        working_group.state = PersistentList(['archived'])
        context.reindex()
        working_group.reindex()
    else:
        default_mode = root.get_default_work_mode()
        participants_mini = root.participants_mini
        mode_id = submitted_appstruct.get(
            'work_mode', default_mode.work_id)
        if mode_id:
            working_group.work_mode_id = mode_id

        #Only the vote of the author is considered
        first_vote_registration(
            user, working_group, submitted_appstruct)
        if participants_mini > 1:
            context.state = PersistentList(
                ['open to a working group', 'published'])
            context.reindex()
            # Add Nia comment
            alert_comment_nia(
                context, request, root,
                internal_kind=InternalAlertKind.working_group_alert,
                subject_type='proposal',
                alert_kind='open_to_a_working_group',
                duplication=context
                )
        else:
            context.state = PersistentList(['amendable', 'published'])
            working_group.state = PersistentList(['active'])
            context.reindex()
            working_group.reindex()
            if not hasattr(working_group, 'first_improvement_cycle'):
                working_group.first_improvement_cycle = True

            if not working_group.improvement_cycle_proc:
                improvement_cycle_proc = start_improvement_cycle(context)
                working_group.setproperty(
                    'improvement_cycle_proc', improvement_cycle_proc)

            working_group.improvement_cycle_proc.execute_action(
                context, request, 'votingpublication', {})
            # Add Nia comment
            alert_comment_nia(
                context, request, root,
                internal_kind=InternalAlertKind.working_group_alert,
                subject_type='proposal',
                alert_kind='start_work',
                duplication=context
                )

    related_ideas = context.related_ideas
    for idea in related_ideas:
        # Add Nia comment
        alert_comment_nia(
            idea, request, root,
            internal_kind=InternalAlertKind.working_group_alert,
            subject_type='idea',
            alert_kind='new_proposal',
            proposal_state=proposal_state,
            proposal=context
            )

    if getattr(context, '_tree', None):
        tree = getattr(context, '_tree')
        root.merge_tree(tree)

    context.modified_at = datetime.datetime.now(tz=pytz.UTC)
    context.init_published_at()
    not_published_ideas = []
    if not getattr(root, 'moderate_ideas', False) and\
       'idea' not in getattr(root, 'content_to_examine', []):
        not_published_ideas = [i for i in context.related_ideas
                               if 'published' not in i.state]
        publish_ideas(not_published_ideas, request)

    not_published_ideas.extend(context)
    return not_published_ideas


def publish_ideas(ideas, request):
    for idea in ideas:
        idea.state = PersistentList(['published'])
        idea.modified_at = datetime.datetime.now(tz=pytz.UTC)
        idea.reindex()
        request.registry.notify(ObjectPublished(object=idea))


def publish_condition(process):
    proposal = process.execution_context.created_entity('proposal')
    if proposal:
        working_group = proposal.working_group
        report = working_group.vp_ballot.report
        if not getattr(working_group, 'first_vote', True):
            electeds = report.get_electeds()
            if electeds is None:
                return False
            else:
                return True

        report.calculate_votes()
        if report.result['False'] != 0:
            return False

    return True


def start_improvement_cycle(proposal):
    def_container = find_service('process_definition_container')
    runtime = find_service('runtime')
    pd = def_container.get_definition('proposalimprovementcycle')
    proc = pd()
    proc.__name__ = proc.id
    runtime.addtoproperty('processes', proc)
    proc.defineGraph(pd)
    proc.execution_context.add_created_entity('proposal', proposal)
    proc.execute()
    return proc


def first_vote_registration(user, working_group, appstruct):
    #duration vote
    ballot = working_group.duration_configuration_ballot
    report = ballot.report
    if user not in report.voters:
        elected_id = appstruct['elected']
        try:
            subject_id = get_oid(elected_id[OBJECT_DATA])
        except Exception:
            subject_id = elected_id
        votefactory = report.ballottype.vote_factory
        vote = votefactory(subject_id)
        vote.user_id = get_oid(user)
        ballot.ballot_box.addtoproperty('votes', vote)
        report.addtoproperty('voters', user)
    #publication vote
    ballot = working_group.vp_ballot
    report = ballot.report
    if user not in report.voters:
        vote = appstruct.get('vote', False)
        votefactory = report.ballottype.vote_factory
        vote = votefactory(vote)
        vote.user_id = get_oid(user)
        ballot.ballot_box.addtoproperty('votes', vote)
        report.addtoproperty('voters', user)


def first_vote_remove(user, working_group):
    user_oid = get_oid(user)
    #duration vote
    ballot = working_group.duration_configuration_ballot
    votes = [v for v in ballot.ballot_box.votes
             if getattr(v, 'user_id', 0) == user_oid]
    if votes:
        ballot.ballot_box.delfromproperty('votes', votes[0])
        ballot.report.delfromproperty('voters', user)

    #publication vote
    ballot = working_group.vp_ballot
    votes = [v for v in ballot.ballot_box.votes
             if getattr(v, 'user_id', 0) == user_oid]
    if votes:
        ballot.ballot_box.delfromproperty('votes', votes[0])
        ballot.report.delfromproperty('voters', user)


def calculate_improvement_cycle_duration(process):
    if getattr(process, 'attachedTo', None):
        process = process.attachedTo.process

    proposal = process.execution_context.created_entity('proposal')
    working_group = proposal.working_group
    duration_ballot = getattr(
        working_group, 'duration_configuration_ballot', None)
    if duration_ballot is not None and duration_ballot.report.voters:
        electeds = duration_ballot.report.get_electeds()
        if electeds:
            return AMENDMENTS_CYCLE_DEFAULT_DURATION[electeds[0]]

    return AMENDMENTS_CYCLE_DEFAULT_DURATION["One week"]


def publish_proposal_moderation(context, request, root, **kw):
    user = context.author
    context.state.remove('submitted')
    submitted_appstruct = getattr(context, 'submitted_appstruct', {})
    not_published_ideas = confirm_proposal(
        context, request, user, submitted_appstruct, root)
    alert('internal', [root], [user],
          internal_kind=InternalAlertKind.moderation_alert,
          subjects=[context], alert_kind='moderation',
          ballot=kw.get('ballot_url', ''))
    if getattr(user, 'email', ''):
        mail_template = root.get_mail_template(
            'publish_proposal_decision', user.user_locale)
        subject = mail_template['subject'].format(
            subject_title=context.title)
        email_data = get_user_data(user, 'recipient', request)
        email_data.update(get_entity_data(context, 'subject', request))
        message = mail_template['template'].format(
            novaideo_title=root.title,
            **email_data
        )
        alert('email', [root.get_site_sender()], [user.email],
              subject=subject, body=message)

    request.registry.notify(ObjectPublished(object=context))
    return not_published_ideas


def archive_proposal_moderation(context, request, root, appstruct, **kw):
    explanation = appstruct['explanation']
    context.state = PersistentList(['archived'])
    context.reindex()
    user = context.author
    alert('internal', [root], [user],
          internal_kind=InternalAlertKind.moderation_alert,
          subjects=[context], alert_kind='moderation',
          ballot=kw.get('ballot_url', ''))
    if getattr(user, 'email', ''):
        mail_template = root.get_mail_template(
            'archive_proposal_decision', user.user_locale)
        subject = mail_template['subject'].format(
            subject_title=context.title)
        email_data = get_user_data(user, 'recipient', request)
        email_data.update(get_entity_data(context, 'subject', request))
        message = mail_template['template'].format(
            explanation=explanation,
            novaideo_title=root.title,
            **email_data
        )
        alert('email', [root.get_site_sender()], [user.email],
              subject=subject, body=message)


def exclude_participant_from_wg(context, request,  user, root, kind='resign', **kw):
    working_group = context.working_group
    working_group.delfromproperty('members', user)
    remove_participant_from_ballots(context, request, user)
    members = working_group.members
    revoke_roles(user, (('Participant', context),))
    subject_data = get_entity_data(context, 'subject', request)
    if members:
        alert_data = get_user_data(user, 'participant', request)
        alert_data.update(get_entity_data(user, 'participant', request))
        alert_data.update(subject_data)
        alert(
            'internal', [root], members,
            internal_kind=InternalAlertKind.working_group_alert,
            subjects=[context], alert_kind=kind,
            ballot=kw.get('ballot_url', ''),
            **alert_data)

    sender = root.get_site_sender()
    if working_group.wating_list:
        def _get_next_user(users):
            for user in users:
                wgs = user.get_active_working_groups(user)
                if 'active' in user.state and \
                   len(wgs) < root.participations_maxi:
                    return user

            return None

        next_user = _get_next_user(working_group.wating_list)
        if next_user is not None:
            mail_template = root.get_mail_template(
                'wg_wating_list_participation',
                next_user.user_locale)
            working_group.delfromproperty('wating_list', next_user)
            working_group.addtoproperty('members', next_user)
            grant_roles(next_user, (('Participant', context),))
            if members:
                alert('internal', [root], members,
                      internal_kind=InternalAlertKind.working_group_alert,
                      subjects=[context],
                      alert_kind='wg_wating_list_participation')

            if getattr(next_user, 'email', ''):
                subject = mail_template['subject'].format(
                    subject_title=context.title)
                email_data = get_user_data(next_user, 'recipient', request)
                email_data.update(subject_data)
                message = mail_template['template'].format(
                    novaideo_title=root.title,
                    **email_data
                )
                alert('email', [sender], [next_user.email],
                      subject=subject, body=message)

    participants = working_group.members
    len_participants = len(participants)
    participants_mini = getattr(root, 'participants_mini', 3)
    if len_participants < participants_mini and \
       'open to a working group' not in context.state:
        context.state = PersistentList(
            ['open to a working group', 'published'])
        working_group.state = PersistentList(['deactivated'])
        working_group.reindex()
        context.reindex()
        alert('internal', [root], participants,
              internal_kind=InternalAlertKind.working_group_alert,
              subjects=[context], alert_kind=kind+'_to_wg_open')
        # Add Nia comment
        alert_comment_nia(
            context, request, root,
            internal_kind=InternalAlertKind.working_group_alert,
            subject_type='proposal',
            alert_kind='exclusion_open_to_a_wg',
            duplication=context
            )

    if getattr(user, 'email', ''):
        alert(
            'internal', [root], [user],
            internal_kind=InternalAlertKind.working_group_alert,
            subjects=[context], alert_kind='wg_'+kind,
            period_date=kw.get('period_date', None),
            **subject_data)
        # mail_template = root.get_mail_template('wg_'+kind)
        # subject = mail_template['subject'].format(
        #     subject_title=context.title)
        # email_data = get_user_data(user, 'recipient', request)
        # email_data.update(subject_data)
        # message = mail_template['template'].format(
        #     novaideo_title=root.title,
        #     **email_data
        # )
        # alert('email', [sender], [user.email],
        #       subject=subject, body=message)

    run_notation_process(
        context, request, user, members, 'member_notation')

    if members:
        alert(
            'internal', [root], [user],
            internal_kind=InternalAlertKind.working_group_alert,
            subjects=[context], alert_kind='member_notation_excluded',
            **subject_data)
        mail_template = root.get_mail_template(
            'member_notation_excluded', user.user_locale)
        subject = mail_template['subject'].format(
            novaideo_title=root.title,
            **subject_data)
        email_data = get_user_data(user, 'recipient', request)
        email_data.update(subject_data)
        message = mail_template['template'].format(
            novaideo_title=root.title,
            **email_data)
        alert('email', [root.get_site_sender()], [user.email],
              subject=subject, body=message)

        for member in members:
            run_notation_process(
                context, request, member, [user])


def calculate_improvement_cycle_date(process):
    return calculate_improvement_cycle_duration(process) + \
        datetime.datetime.now()


def createproposal_roles_validation(process, context):
    return has_role(role=('SiteAdmin',))


def createproposal_processsecurity_validation(process, context):
    request = get_current_request()
    if 'proposal' not in request.content_to_manage:
        return False

    return global_user_processsecurity()


def include_ideas_texts(proposal, related_ideas):
    proposal.text = getattr(proposal, 'text', '') +\
                    ''.join(['<div>' + idea.text + '</div>' \
                             for idea in related_ideas])


class CreateProposal(InfiniteCardinality):
    submission_title = _('Save')
    context = INovaIdeoApplication
    roles_validation = createproposal_roles_validation
    processsecurity_validation = createproposal_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        user = get_current(request)
        mask = user.get_mask(root)
        author = mask if appstruct.get('anonymous', False) and mask else user
        related_ideas = appstruct.pop('related_ideas')
        proposal = appstruct['_object_data']
        proposal.text = html_diff_wrapper.normalize_text(proposal.text)
        root.addtoproperty('proposals', proposal)
        proposal.state.append('draft')
        grant_roles(user=author, roles=(('Owner', proposal), ))
        grant_roles(user=author, roles=(('Participant', proposal), ))
        proposal.setproperty('author', author)
        wg = WorkingGroup()
        root.addtoproperty('working_groups', wg)
        wg.init_workspace()
        wg.setproperty('proposal', proposal)
        wg.addtoproperty('members', author)
        wg.state.append('deactivated')
        if related_ideas:
            connect(proposal,
                    related_ideas,
                    {'comment': _('Add related ideas'),
                     'type': _('Creation')},
                    author,
                    ['related_proposals', 'related_ideas'],
                    CorrelationType.solid)

        #TODO Add Nia comment to related ideas
        add_attached_files(appstruct, proposal)
        proposal.reindex()
        init_proposal_ballots(proposal)
        wg.reindex()
        proposal.subscribe_to_channel(user)
        request.registry.notify(ActivityExecuted(self, [proposal, wg], author))
        return {'newcontext': proposal}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(kw['newcontext'], "@@index"))


def pap_processsecurity_validation(process, context):
    request = get_current_request()
    if 'proposal' not in request.content_to_manage:
        return False

    condition = False
    if 'idea' in request.content_to_examine:
        condition = 'favorable' in context.state
    else:
        condition = 'published' in context.state

    return condition and has_role(role=('Member',))


class PublishAsProposal(CreateProposal):
    style = 'button' #TODO add style abstract class
    context = Iidea
    submission_title = _('Save')
    style_order = 0
    style_descriminator = 'primary-action'
    style_picto = 'novaideo-icon icon-wg'
    processsecurity_validation = pap_processsecurity_validation
    roles_validation = NotImplemented


def del_processsecurity_validation(process, context):
    return global_user_processsecurity() and \
           (has_role(role=('Owner', context)) and \
           'draft' in context.state)


class DeleteProposal(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-trash'
    style_order = 12
    submission_title = _('Continue')
    context = IProposal
    processsecurity_validation = del_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        not_draft_owner = 'draft' not in context.state or \
                          not has_role(role=('Owner', context))
        context.remove_tokens()
        wg = context.working_group
        members = list(wg.members)
        for member in members:
            wg.delfromproperty('members', member)

        wg.delfromproperty('proposal', context)
        root.delfromproperty('working_groups', wg)
        request.registry.notify(CorrelableRemoved(object=context))
        root.delfromproperty('proposals', context)
        if not_draft_owner:
            explanation = appstruct['explanation']
            alert('internal', [root], members,
                  internal_kind=InternalAlertKind.moderation_alert,
                  subjects=[], removed=True, subject_title=context.title)
            subject_data = get_entity_data(context, 'subject', request)
            for member in members:
                if getattr(member, 'email', ''):
                    mail_template = root.get_mail_template(
                        'delete_proposal', member.user_locale)
                    subject = mail_template['subject'].format(
                        subject_title=context.title)
                    email_data = get_user_data(member, 'recipient', request)
                    email_data.update(subject_data)
                    message = mail_template['template'].format(
                        explanation=explanation,
                        novaideo_title=root.title,
                        **email_data
                    )
                    alert('email', [root.get_site_sender()], [member.email],
                          subject=subject, body=message)

        return {'newcontext': root}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(kw['newcontext'], ""))


def pu_sub_processsecurity_validation(process, context):
    user = get_current()
    root = getSite()
    not_published_ideas = False
    if getattr(root, 'moderate_ideas', False):
        not_published_ideas = any('published' not in i.state
                                  for i in context.related_ideas)

    not_favorable_ideas = False
    if 'idea' in getattr(root, 'content_to_examine', []):
        not_favorable_ideas = any('favorable' not in i.state
                                  for i in context.related_ideas)

    return not (not_published_ideas or not_favorable_ideas) and \
           len(user.get_active_working_groups(user)) < root.participations_maxi and \
           global_user_processsecurity()


def submit_roles_validation(process, context):
    return has_role(role=('Owner', context))


def submit_processsecurity_validation(process, context):
    request = get_current_request()
    if not request.moderate_proposals:
        return False

    return pu_sub_processsecurity_validation(process, context)


def submit_state_validation(process, context):
    return 'draft' in context.state


class SubmitProposalModeration(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-share'
    style_order = 6
    submission_title = _('Continue')
    context = IProposal
    roles_validation = submit_roles_validation
    processsecurity_validation = submit_processsecurity_validation
    state_validation = submit_state_validation

    def start(self, context, request, appstruct, **kw):
        context.state = PersistentList(['submitted'])
        context.submitted_appstruct = PersistentDict(appstruct)
        context.reindex()
        root = getSite()
        # get random moderators
        moderators = get_random_users(ELECTORS_NB, [context.author])
        if not moderators:
            not_published_ideas = publish_proposal_moderation(
                context, request, root)
            request.registry.notify(ActivityExecuted(
                self, not_published_ideas, get_current()))
        else:
            author = context.author
            start_ballot(
                context, author, request, root,
                moderators, 'proposalmoderation',
                initiator=get_current(),
                subjects=[context])
            alert_data = get_ballot_alert_data(
                context, request, root, moderators)
            alert_data.update(get_user_data(author, 'recipient', request))
            mail_template = root.get_mail_template(
                'publish_proposal_decision', author.user_locale)
            subject = mail_template['subject'].format(
                subject_title=context.title)
            email_data = get_user_data(author, 'recipient', request)
            email_data.update(get_entity_data(context, 'subject', request))
            message = mail_template['template'].format(
                novaideo_title=root.title,
                **email_data
            )
            alert('email', [root.get_site_sender()], [author.email],
                  subject=subject, body=message)

        request.registry.notify(ObjectPublished(object=context))
        request.registry.notify(ActivityExecuted(
            self, not_published_ideas, get_current()))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def publish_roles_validation(process, context):
    return has_role(role=('Owner', context))


def publish_processsecurity_validation(process, context):
    request = get_current_request()
    if request.moderate_proposals:
        return False
    return pu_sub_processsecurity_validation(process, context)


def publish_state_validation(process, context):
    return "draft" in context.state


class PublishProposal(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-share'
    style_order = 13
    submission_title = _('Continue')
    context = IProposal
    roles_validation = publish_roles_validation
    processsecurity_validation = publish_processsecurity_validation
    state_validation = publish_state_validation

    def start(self, context, request, appstruct, **kw):
        user = context.author
        root = getSite()
        context.state.remove('draft')
        # Share the proposal with the specified members 
        # we need to execute the 'present' action
        members_to_invite = appstruct.get('members_to_invite', [])
        if members_to_invite:
            present_actions = self.process.get_actions('present')
            present_action = present_actions[0] if present_actions else None
            if present_action:
                mail_template = root.get_mail_template(
                    'presentation_proposal', user.user_locale)
                email_data = get_user_data(user, 'my', request)
                email_data.update(get_entity_data(context, 'subject', request))
                message = mail_template['template'].format(
                    recipient_title='',
                    recipient_first_name='',
                    recipient_last_name='',
                    novaideo_title=root.title,
                    **email_data
                )
                data = {
                    'members': members_to_invite,
                    'send_to_me': False,
                    'subject': mail_template['subject'].format(
                        subject_title=context.title),
                    'message': message,
                }
                result = present_action.start(context, request, data, **kw)

        not_published_ideas = confirm_proposal(
            context, request, user, appstruct, root)
        request.registry.notify(ObjectPublished(object=context))
        request.registry.notify(ActivityExecuted(
            self, not_published_ideas, user))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def duplicate_processsecurity_validation(process, context):
    return 'draft' not in context.state and \
           global_user_processsecurity()


class DuplicateProposal(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_picto = 'octicon octicon-git-branch'
    style_order = 7
    submission_title = _('Save')
    context = IProposal
    processsecurity_validation = duplicate_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        user = get_current(request)
        mask = user.get_mask(root)
        author = mask if appstruct.pop('anonymous', False) and mask else user
        related_ideas = appstruct.pop('related_ideas')
        copy_of_proposal = copy(
            context, (root, 'proposals'),
            omit=('created_at', 'modified_at',
                  'examined_at', 'published_at',
                  'opinion', 'attached_files',
                  'len_selections', 'graph'))
        copy_of_proposal.opinion = PersistentDict({})
        copy_of_proposal.init_graph()
        copy_of_proposal.set_data(appstruct)
        copy_of_proposal.text = html_diff_wrapper.normalize_text(
            copy_of_proposal.text)
        copy_of_proposal.setproperty('originalentity', context)
        copy_of_proposal.state = PersistentList(['draft'])
        grant_roles(user=author, roles=(('Owner', copy_of_proposal), ))
        grant_roles(user=author, roles=(('Participant', copy_of_proposal), ))
        copy_of_proposal.setproperty('author', author)
        wg = WorkingGroup()
        root.addtoproperty('working_groups', wg)
        wg.init_workspace()
        wg.setproperty('proposal', copy_of_proposal)
        wg.addtoproperty('members', author)
        wg.state.append('deactivated')
        if related_ideas:
            connect(copy_of_proposal,
                    related_ideas,
                    {'comment': _('Add related ideas'),
                     'type': _('Duplicate')},
                    author,
                    ['related_proposals', 'related_ideas'],
                    CorrelationType.solid)

        add_attached_files(appstruct, copy_of_proposal)
        wg.reindex()
        copy_of_proposal.reindex()
        init_proposal_ballots(copy_of_proposal)
        context.reindex()
        request.registry.notify(ActivityExecuted(
            self, [copy_of_proposal, wg], author))
        copy_of_proposal.subscribe_to_channel(user)
        return {'newcontext': copy_of_proposal}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(kw['newcontext'], "@@index"))


def edit_roles_validation(process, context):
    return has_role(role=('Owner', context))


def edit_processsecurity_validation(process, context):
    return global_user_processsecurity()


def edit_state_validation(process, context):
    return "draft" in context.state


class EditProposal(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'text-action'
    style_picto = 'glyphicon glyphicon-pencil'
    style_order = 1
    submission_title = _('Save')
    context = IProposal
    roles_validation = edit_roles_validation
    processsecurity_validation = edit_processsecurity_validation
    state_validation = edit_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        user = context.author
        if 'related_ideas' in appstruct:
            context.set_related_ideas(
                appstruct['related_ideas'], user)

        add_attached_files(appstruct, context)
        context.text = html_diff_wrapper.normalize_text(context.text)
        context.modified_at = datetime.datetime.now(tz=pytz.UTC)
        context.reindex()
        request.registry.notify(ActivityExecuted(self, [context], user))
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def support_roles_validation(process, context):
    return has_role(role=('Member',))


def support_processsecurity_validation(process, context):
    user = get_current()
    request = get_current_request()
    if not request.support_proposals:
        return False

    return context.evaluation(user) != Evaluations.support and \
           (context.user_has_token(user) or  \
            context.evaluation(user) == Evaluations.oppose) and \
           global_user_processsecurity()


def support_state_validation(process, context):
    return 'submitted_support' in context.state


class SupportProposal(InfiniteCardinality):
    # style = 'button' #TODO add style abstract class
    # style_descriminator = 'text-action'
    # style_picto = 'glyphicon glyphicon-thumbs-up'
    # style_order = 4
    context = IProposal
    roles_validation = support_roles_validation
    processsecurity_validation = support_processsecurity_validation
    state_validation = support_state_validation

    def start(self, context, request, appstruct, **kw):
        user = get_current(request)
        context.init_support_history()
        if context.evaluation(user):
            user.remove_token(context)
            context.remove_token(user)
            context._support_history.append(
                (get_oid(user), datetime.datetime.now(tz=pytz.UTC), -1))

        user.add_token(context, Evaluations.support, request.root)
        context.add_token(user, Evaluations.support)
        context._support_history.append(
            (get_oid(user), datetime.datetime.now(tz=pytz.UTC), 1))
        context.reindex()
        request.registry.notify(ActivityExecuted(self, [context], user))
        users = list(get_users_by_preferences(context))
        users.extend(context.working_group.members)
        alert('internal', [request.root], users,
              internal_kind=InternalAlertKind.support_alert,
              subjects=[context], support_kind='support')
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))



def oppose_processsecurity_validation(process, context):
    user = get_current()
    request = get_current_request()
    if not request.support_proposals:
        return False

    return context.evaluation(user) != Evaluations.oppose and \
           (context.user_has_token(user) or  \
            context.evaluation(user) == Evaluations.support) and \
           global_user_processsecurity()


class OpposeProposal(InfiniteCardinality):
    # style = 'button' #TODO add style abstract class
    # style_descriminator = 'text-action'
    # style_picto = 'glyphicon glyphicon-thumbs-down'
    # style_order = 5
    context = IProposal
    roles_validation = support_roles_validation
    processsecurity_validation = oppose_processsecurity_validation
    state_validation = support_state_validation

    def start(self, context, request, appstruct, **kw):
        user = get_current(request)
        context.init_support_history()
        if context.evaluation(user):
            user.remove_token(context)
            context.remove_token(user)
            context._support_history.append(
                (get_oid(user), datetime.datetime.now(tz=pytz.UTC), -1))

        user.add_token(context, Evaluations.oppose, request.root)
        context.add_token(user, Evaluations.oppose)
        context._support_history.append(
            (get_oid(user), datetime.datetime.now(tz=pytz.UTC), 0))
        context.reindex()
        request.registry.notify(ActivityExecuted(self, [context], user))
        users = list(get_users_by_preferences(context))
        users.extend(context.working_group.members)
        alert('internal', [request.root], users,
              internal_kind=InternalAlertKind.support_alert,
              subjects=[context], support_kind='oppose')
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def opinion_roles_validation(process, context):
    return has_role(role=('Examiner',))


def opinion_processsecurity_validation(process, context):
    request = get_current_request()
    if 'proposal' not in request.content_to_examine:
        return False

    return global_user_processsecurity()


def opinion_state_validation(process, context):
    return 'submitted_support' in context.state and 'examined' not in context.state


class MakeOpinion(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'octicon octicon-checklist'
    style_order = 10
    submission_title = _('Save')
    context = IProposal
    roles_validation = opinion_roles_validation
    processsecurity_validation = opinion_processsecurity_validation
    state_validation = opinion_state_validation

    def start(self, context, request, appstruct, **kw):
        appstruct.pop('_csrf_token_')
        context.opinion = PersistentDict(appstruct)
        context.state = PersistentList(
            ['examined', 'published', context.opinion['opinion']])
        context.init_examined_at()
        context.reindex()
        context.remove_tokens()
        members = context.working_group.members
        root = getSite()
        localizer = request.localizer
        users = list(get_users_by_preferences(context))
        users.extend(members)
        alert('internal', [root], users,
              internal_kind=InternalAlertKind.examination_alert,
              subjects=[context])
        # Add Nia comment
        alert_comment_nia(
            context, request, root,
            internal_kind=InternalAlertKind.examination_alert,
            subject_type='proposal'
            )
        subject_data = get_entity_data(context, 'subject', request)
        for member in members:
            if getattr(member, 'email', ''):
                mail_template = root.get_mail_template(
                    'opinion_proposal', member.user_locale)
                subject = mail_template['subject'].format(subject_title=context.title)
                email_data = get_user_data(member, 'recipient', request)
                email_data.update(subject_data)
                message = mail_template['template'].format(
                    opinion=localizer.translate(_(context.opinion_value)),
                    explanation=context.opinion['explanation'],
                    novaideo_title=request.root.title,
                    **email_data
                )
                alert('email', [root.get_site_sender()], [member.email],
                      subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context], get_current(request)))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def withdrawt_processsecurity_validation(process, context):
    return context.evaluation(get_current()) and \
           global_user_processsecurity()


class WithdrawToken(InfiniteCardinality):
    # style = 'button' #TODO add style abstract class
    # style_descriminator = 'text-action'
    # style_picto = 'glyphicon glyphicon-share-alt'
    # style_order = 6
    context = IProposal
    roles_validation = support_roles_validation
    processsecurity_validation = withdrawt_processsecurity_validation
    state_validation = support_state_validation

    def start(self, context, request, appstruct, **kw):
        user = get_current(request)
        user.remove_token(context)
        context.remove_token(user)
        context.init_support_history()
        context._support_history.append(
            (get_oid(user), datetime.datetime.now(tz=pytz.UTC), -1))
        context.reindex()
        request.registry.notify(ActivityExecuted(self, [context], user))
        users = list(get_users_by_preferences(context))
        users.extend(context.working_group.members)
        alert('internal', [request.root], users,
              internal_kind=InternalAlertKind.support_alert,
              subjects=[context], support_kind='withdraw')
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def comm_relation_validation(process, context):
    return process.execution_context.has_relation(context, 'proposal')


def comm_roles_validation(process, context):
    return has_role(role=('Member',))


def comm_processsecurity_validation(process, context):
    root = getSite()
    if not root.manage_proposals:
        return False

    return global_user_processsecurity()


def comm_state_validation(process, context):
    return 'draft' not in context.state and \
        'censored' not in context.state


class CommentProposal(CommentIdea):
    context = IProposal
    roles_validation = comm_roles_validation
    processsecurity_validation = comm_processsecurity_validation
    state_validation = comm_state_validation


def comma_roles_validation(process, context):
    return has_role(role=('Anonymous',), ignore_superiors=True)


def comma_processsecurity_validation(process, context):
    return True


class CommentProposalAnonymous(CommentProposal):
    roles_validation = comma_roles_validation
    processsecurity_validation = comma_processsecurity_validation
    style_interaction = 'ajax-action'
    style_interaction_type = 'popover'

    def start(self, context, request, appstruct, **kw):
        return {}


def seea_roles_validation(process, context):
    return has_role(role=('Participant', context))


def seea_processsecurity_validation(process, context):
    return any(not('archived' in a.state) for a in context.amendments) and \
          global_user_processsecurity()


class SeeAmendments(InfiniteCardinality):
    isSequential = False
    context = IProposal
    roles_validation = seea_roles_validation
    processsecurity_validation = seea_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def seem_processsecurity_validation(process, context):
    return global_user_processsecurity()


class SeeMembers(InfiniteCardinality):
    style_descriminator = 'listing-wg-action'
    style_interaction = 'ajax-action'
    style_interaction_type = 'slider'
    style_picto = 'fa fa-users'
    isSequential = False
    context = IProposal
    processsecurity_validation = seem_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def present_roles_validation(process, context):
    return has_role(role=('Member',))


def present_processsecurity_validation(process, context):
    return global_user_processsecurity()


def present_state_validation(process, context):
    return 'draft' not in context.state and \
        'censored' not in context.state


class PresentProposal(PresentIdea):
    context = IProposal
    roles_validation = present_roles_validation
    processsecurity_validation = present_processsecurity_validation
    state_validation = present_state_validation


def presenta_roles_validation(process, context):
    return has_role(role=('Anonymous',), ignore_superiors=True)


def presenta_processsecurity_validation(process, context):
    return True


class PresentProposalAnonymous(PresentProposal):
    roles_validation = presenta_roles_validation
    processsecurity_validation = presenta_processsecurity_validation
    style_interaction = 'ajax-action'
    style_interaction_type = 'popover'

    def start(self, context, request, appstruct, **kw):
        return {}


def associate_processsecurity_validation(process, context):
    return (has_role(role=('Owner', context)) or \
           (has_role(role=('Member',)) and \
            'draft' not in context.state)) and \
           global_user_processsecurity()


class Associate(AssociateIdea):
    context = IProposal
    processsecurity_validation = associate_processsecurity_validation


def seeideas_state_validation(process, context):
    return 'draft' not in context.state or \
           ('draft' in context.state and has_role(role=('Owner', context)))


class SeeRelatedIdeas(InfiniteCardinality):
    style_descriminator = 'listing-primary-action'
    style_interaction = 'ajax-action'
    style_interaction_type = 'slider'
    # style_interaction_container = 'modal-l'
    style_picto = 'glyphicon glyphicon-link'
    context = IProposal
    #processsecurity_validation = seeideas_processsecurity_validation
    #roles_validation = seeideas_roles_validation
    state_validation = seeideas_state_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def withdraw_roles_validation(process, context):
    return has_role(role=('Member',))


def withdraw_processsecurity_validation(process, context):
    user = get_current()
    wg = context.working_group
    return wg and\
           wg.in_wating_list(user) and \
           global_user_processsecurity()


def withdraw_state_validation(process, context):
    return 'amendable' in context.state


class Withdraw(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'wg-action'
    style_order = 3
    style_css_class = 'btn-warning'
    isSequential = False
    context = IProposal
    roles_validation = withdraw_roles_validation
    processsecurity_validation = withdraw_processsecurity_validation
    state_validation = withdraw_state_validation

    def start(self, context, request, appstruct, **kw):
        user = get_current(request)
        working_group = context.working_group
        member = working_group.get_member_in_wating_list(user)
        working_group.delfromproperty('wating_list', member)
        if getattr(member, 'email', ''):
            root = getSite()
            mail_template = root.get_mail_template(
                'withdeaw', member.user_locale)
            subject = mail_template['subject'].format(
                subject_title=context.title)
            email_data = get_user_data(member, 'recipient', request)
            email_data.update(get_entity_data(context, 'subject', request))
            message = mail_template['template'].format(
                novaideo_title=request.root.title,
                **email_data
            )
            alert('email', [root.get_site_sender()], [member.email],
                  subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context, working_group], member))
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def resign_roles_validation(process, context):
    working_group = context.working_group
    return working_group and working_group.get_member(get_current()) is not None


def resign_processsecurity_validation(process, context):
    return global_user_processsecurity()


def resign_state_validation(process, context):
    return any(s in context.state for s in
               ['amendable', 'open to a working group'])


class Resign(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'wg-action'
    style_interaction = 'ajax-action'
    style_order = 2
    style_picto = 'octicon octicon-sign-out'
    style_css_class = 'btn-danger'
    submission_title = _('Continue')
    isSequential = False
    context = IProposal
    roles_validation = resign_roles_validation
    processsecurity_validation = resign_processsecurity_validation
    state_validation = resign_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        user = context.working_group.get_member(get_current(request))
        exclude_participant_from_wg(context, request, user, root)
        request.registry.notify(ActivityExecuted(
            self, [context, context.working_group], user))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def participate_roles_validation(process, context):
    user = get_current()
    working_group = context.working_group
    return working_group and has_role(user=user, role=('Member',)) and \
        not working_group.is_member(user)


def participate_processsecurity_validation(process, context):
    root = getSite()
<<<<<<< HEAD
    user = get_current()
    working_group = context.working_group
    participations = getattr(user, 'wg_participations', [])
    wgs = getattr(user, 'active_working_groups', [])
    if not working_group or user in working_group.wating_list or \
        user in working_group.wating_list_participation or \
        len(wgs) + len(participations) >= root.participations_maxi or \
        not global_user_processsecurity():
        return False

    exclusion_ballots = [b for b in context.ballots
                         if b.group_id == 'vote_exclusion']
    is_excluded = any(user in b.subjects for b in exclusion_ballots
                      if b.is_finished and b.decision_is_valide)
    if is_excluded:
        return False

    participation_ballots = [b for b in context.ballots
                             if b.group_id == 'vote_participation'
                             and b.is_finished and user in b.subjects
                             and b.report.get_electeds() is None
                             and b.decision_is_valide]
    return len(participation_ballots) <= 0
=======
    wgs = user.get_active_working_groups(user) \
        if hasattr(user, 'get_active_working_groups') else []
    return working_group and \
       not working_group.in_wating_list(user) and \
       len(wgs) < root.participations_maxi and \
       global_user_processsecurity()
>>>>>>> bad3d99a... add anonymous mode


def participate_state_validation(process, context):
    working_group = context.working_group
    return working_group and \
        not('closed' in working_group.state) and \
        any(s in context.state for s in
            ['amendable', 'open to a working group'])


def accept_participation(context, request, user, root, **kw):
    def _send_mail_to_user(
        subject_template, message_template,
        user, context, request):
        subject = subject_template.format(subject_title=context.title)
        email_data = get_user_data(user, 'recipient', request)
        email_data.update(get_entity_data(context, 'subject', request))
        message = message_template.format(
            novaideo_title=request.root.title,
            **email_data
        )
        alert('email', [request.root.get_site_sender()], [user.email],
              subject=subject, body=message)

    working_group = context.working_group
    participants = working_group.members
    participants_mini = getattr(root, 'participants_mini', 3)
    mode = getattr(working_group, 'work_mode', root.get_default_work_mode())
    len_participants = len(participants)
    if user in working_group.wating_list_participation:
        working_group.delfromproperty('wating_list_participation', user)

    if len_participants < mode.participants_maxi:
        #Alert new participant
        if participants:
            alert('internal', [root], participants,
                  internal_kind=InternalAlertKind.working_group_alert,
                  subjects=[context], alert_kind='participate',
                  ballot=kw.get('ballot_url', ''))

        working_group.addtoproperty('members', user)
        grant_roles(user, (('Participant', context),))
        #alert max working groups
        active_wgs = getattr(user, 'active_working_groups', [])
        if len(active_wgs) == root.participations_maxi:
            alert('internal', [root], [user],
                  internal_kind=InternalAlertKind.working_group_alert,
                  subjects=[user], alert_kind='participations_maxi')

        if (len_participants+1) == participants_mini:
            working_group.state = PersistentList(['active'])
            context.state = PersistentList(['amendable', 'published'])
            working_group.reindex()
            context.reindex()
            #Only if is the first improvement cycle
            if not hasattr(working_group, 'first_improvement_cycle'):
                working_group.first_improvement_cycle = True
                if not working_group.improvement_cycle_proc:
                    improvement_cycle_proc = start_improvement_cycle(
                        context)
                    working_group.setproperty(
                        'improvement_cycle_proc', improvement_cycle_proc)

                #Run the improvement cycle proc
                working_group.improvement_cycle_proc.execute_action(
                    context, request, 'votingpublication', {})

            #Alert start of the improvement cycle proc
            alert('internal', [root], participants,
                  internal_kind=InternalAlertKind.working_group_alert,
                  subjects=[context], alert_kind='amendable')

        #Send Mail alert to user
        if getattr(user, 'email', ''):
            mail_template = root.get_mail_template(
                'wg_participation', user.user_locale)
            _send_mail_to_user(
                mail_template['subject'], mail_template['template'],
                user, context, request)

        alert('internal', [root], [user],
              internal_kind=InternalAlertKind.working_group_alert,
              subjects=[context], alert_kind='accepted_participation')

    else:
        working_group.addtoproperty('wating_list', user)
        working_group.reindex()
        users = list(participants)
        users.append(user)
        alert('internal', [root], users,
              internal_kind=InternalAlertKind.working_group_alert,
              subjects=[context], alert_kind='wg_participation_max')

        if getattr(user, 'email', ''):
            mail_template = root.get_mail_template(
                'wating_list', user.user_locale)
            _send_mail_to_user(
                mail_template['subject'], mail_template['template'],
                user, context, request)


class Participate(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'wg-action'
    style_interaction = 'ajax-action'
    style_order = 1
    style_picto = 'typcn typcn-user-add'
    style_css_class = 'btn-success'
    submission_title = _('Continue')
    isSequential = False
    context = IProposal
    roles_validation = participate_roles_validation
    processsecurity_validation = participate_processsecurity_validation
    state_validation = participate_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        user = get_current(request)
        mask = user.get_mask(root)
        member = mask if appstruct.get('anonymous', False) and mask else user

        working_group = context.working_group
<<<<<<< HEAD
        if not getattr(root, 'working_group_composition_control', True):
            accept_participation(context, request, user, root)
        else:
            moderators = working_group.members
            if not moderators:
                accept_participation(context, request, user, root)
            else:
                working_group.addtoproperty('wating_list_participation', user)

                def before_start(b_proc):
                    b_proc.participant = user

                start_ballot(
                    context, user, request, root,
                    moderators, 'proposalparticipation',
                    before_start=before_start,
                    initiator=user,
                    subjects=[user])
                alert_data = get_ballot_alert_data(
                    context, request, root, moderators)
                alert('internal', [root], [user],
                      internal_kind=InternalAlertKind.working_group_alert,
                      alert_kind='member_participation',
                      subjects=[context], **alert_data)
        request.registry.notify(ActivityExecuted(
            self, [context, working_group], user))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def exclude_roles_validation(process, context):
    return has_role(role=('Participant', context))

=======
        participants = working_group.members
        mode = getattr(working_group, 'work_mode', root.get_default_work_mode())
        len_participants = len(participants)
        if len_participants < mode.participants_maxi:
            #Alert new participant
            if participants:
                alert('internal', [root], participants,
                      internal_kind=InternalAlertKind.working_group_alert,
                      subjects=[context], alert_kind='participate')

            working_group.addtoproperty('members', member)
            grant_roles(member, (('Participant', context),))
            #alert maw working groups
            active_wgs = user.get_active_working_groups(user) \
                if hasattr(user, 'get_active_working_groups') else []
            if len(active_wgs) == root.participations_maxi:
                alert('internal', [root], [member],
                      internal_kind=InternalAlertKind.working_group_alert,
                      subjects=[member], alert_kind='participations_maxi')

            if (len_participants+1) == mode.participants_mini:
                working_group.state = PersistentList(['active'])
                context.state = PersistentList(['amendable', 'published'])
                working_group.reindex()
                context.reindex()
                #Only if is the first improvement cycle
                if not hasattr(working_group, 'first_improvement_cycle'):
                    working_group.first_improvement_cycle = True
                    if not working_group.improvement_cycle_proc:
                        improvement_cycle_proc = start_improvement_cycle(
                            context)
                        working_group.setproperty(
                            'improvement_cycle_proc', improvement_cycle_proc)

                    #Run the improvement cycle proc
                    working_group.improvement_cycle_proc.execute_action(
                        context, request, 'votingpublication', {})

                #Alert start of the improvement cycle proc
                alert('internal', [root], participants,
                      internal_kind=InternalAlertKind.working_group_alert,
                      subjects=[context], alert_kind='amendable')
                # Add Nia comment
                alert_comment_nia(
                    context, request, root,
                    internal_kind=InternalAlertKind.working_group_alert,
                    subject_type='proposal',
                    alert_kind='start_work',
                    duplication=context
                    )

            #Send Mail alert to user
            if getattr(member, 'email', ''):
                mail_template = root.get_mail_template(
                    'wg_participation', member.user_locale)
                self._send_mail_to_user(
                    mail_template['subject'], mail_template['template'],
                    user, context, request)
        else:
            working_group.addtoproperty('wating_list', user)
            working_group.reindex()
            users = list(participants)
            users.append(member)
            alert('internal', [root], users,
                  internal_kind=InternalAlertKind.working_group_alert,
                  subjects=[context], alert_kind='wg_participation_max')

            if getattr(member, 'email', ''):
                mail_template = root.get_mail_template(
                    'wating_list', member.user_locale)
                self._send_mail_to_user(
                    mail_template['subject'], mail_template['template'],
                    user, context, request)
>>>>>>> bad3d99a... add anonymous mode

def exclude_processsecurity_validation(process, context):
    working_group = context.working_group
    root = getSite()
    if not working_group or not getattr(
       root, 'working_group_composition_control', False):
        return False

    user = get_current()
    exclusion_ballots = [b for b in context.ballots
                         if b.group_id == 'vote_exclusion']
    start_process = any(b.initiator is user
                        for b in exclusion_ballots
                        if not b.is_finished)
    if start_process:
        return False

    member_exclusion = [b.subjects[0] for b in exclusion_ballots
                        if b.subjects and
                        (not b.is_finished or b.decision_is_valide)]
    members = [m for m in context.working_group.members
               if m not in member_exclusion]
    return len(members) > 1 and \
        global_user_processsecurity()


def exclude_state_validation(process, context):
    working_group = context.working_group
    return working_group and \
        'amendable' in context.state


class ExcludeParticipant(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'wg-action'
    style_interaction = 'ajax-action'
    style_order = 2
    style_picto = 'octicon octicon-sign-out'
    style_css_class = 'btn-success'
    submission_title = _('Continue')
    isSequential = False
    context = IProposal
    roles_validation = exclude_roles_validation
    processsecurity_validation = exclude_processsecurity_validation
    state_validation = exclude_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        user = get_current()
        user_to_exclure = appstruct['participant']
        working_group = context.working_group
        moderators = working_group.members

        def before_start(b_proc):
            b_proc.participant = user_to_exclure

        start_ballot(
            context, user_to_exclure, request, root,
            moderators, 'exclusionparticipant',
            before_start=before_start,
            initiator=user,
            subjects=[user_to_exclure])
        alert_data = get_ballot_alert_data(
            context, request, root, moderators)
        alert('internal', [root], [user_to_exclure],
              internal_kind=InternalAlertKind.working_group_alert,
              alert_kind='member_exclusion',
              subjects=[context], **alert_data)
        request.registry.notify(ActivityExecuted(
            self, [context, working_group], member))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def compare_processsecurity_validation(process, context):
    return getattr(context, 'version', None) is not None and \
           (has_role(role=('Owner', context)) or \
           (has_role(role=('Member',)) and\
            'draft' not in context.state)) and \
           global_user_processsecurity()


class CompareProposal(InfiniteCardinality):
    title = _('Compare')
    context = IProposal
    processsecurity_validation = compare_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def attach_roles_validation(process, context):
    return has_role(role=('Participant', context))


def attach_processsecurity_validation(process, context):
    return global_user_processsecurity()


def attach_state_validation(process, context):
    wg = context.working_group
    return wg and 'active' in wg.state and 'amendable' in context.state


class AttachFiles(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'text-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-paperclip'
    style_order = 3
    submission_title = _('Save')
    context = IProposal
    roles_validation = attach_roles_validation
    processsecurity_validation = attach_processsecurity_validation
    state_validation = attach_state_validation

    def start(self, context, request, appstruct, **kw):
        add_attached_files({'add_files': appstruct}, context)
        context.reindex()
        user = context.working_group.get_member( get_current(request))
        request.registry.notify(ActivityExecuted(
            self, [context], user))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def get_access_key(obj):
    if 'draft' not in obj.state:
        challenge = getattr(obj, 'challenge', None)
        is_restricted = getattr(challenge, 'is_restricted', False)
        if is_restricted:
            return serialize_roles(
                (('ChallengeParticipant', challenge),
                 'SiteAdmin', 'Admin', 'Moderator'))

        return ['always']
    else:
        return serialize_roles(
            (('Owner', obj), ('LocalModerator', obj), 'SiteAdmin',
                'Admin', 'Moderator'))


def seeproposal_processsecurity_validation(process, context):
    challenge = getattr(context, 'challenge', None)
    is_restricted = getattr(challenge, 'is_restricted', False)
    can_access = True
    if is_restricted:
        can_access = has_role(role=('ChallengeParticipant', challenge))

    return can_access and access_user_processsecurity(process, context) and \
           ('draft' not in context.state or \
            has_any_roles(roles=(('Owner', context), ('LocalModerator', context),
                'SiteAdmin', 'Moderator')))


@access_action(access_key=get_access_key)
class SeeProposal(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'access-action'
    style_interaction = 'ajax-action'
    style_interaction_type = 'sidebar'
    style_picto = 'glyphicon glyphicon-eye-open'
    title = _('Details')
    context = IProposal
    actionType = ActionType.automatic
    processsecurity_validation = seeproposal_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


#*************************** ProposalImprovementCycle process **********************************#


def decision_relation_validation(process, context):
    return process.execution_context.has_relation(context, 'proposal')


def decision_roles_validation(process, context):
    return has_role(role=('SiteAdmin',))


def decision_state_validation(process, context):
    wg = context.working_group
    return wg and 'active' in wg.state and \
           'amendable' in context.state


class VotingPublication(ElementaryAction):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'plus-action'
    style_order = 5
    context = IProposal
    processs_relation_id = 'proposal'
    #actionType = ActionType.system
    relation_validation = decision_relation_validation
    roles_validation = decision_roles_validation
    state_validation = decision_state_validation

    def start(self, context, request, appstruct, **kw):
        context.state.remove(context.state[0])
        context.state.insert(0, 'votes for publishing')
        context.reindex()
        working_group = context.working_group
        duration = getattr(working_group, 'work_duration', None)
        working_group.inc_iteration()
        if duration and duration >= datetime.timedelta(weeks=1):
            working_group.inc_nonproductive_cycle()

        if not getattr(working_group, 'first_vote', True):
            members = working_group.members
            root = getSite()
            alert('internal', [root], members,
                  internal_kind=InternalAlertKind.working_group_alert,
                  subjects=[context], alert_kind='end_work')
            subject_data = get_entity_data(context, 'subject', request)
            for member in members:
                if getattr(member, 'email', ''):
                    mail_template = root.get_mail_template(
                        'start_vote_publishing', member.user_locale)
                    subject = mail_template['subject'].format(
                        subject_title=context.title)
                    email_data = get_user_data(member, 'recipient', request)
                    email_data.update(subject_data)
                    message = mail_template['template'].format(
                        novaideo_title=root.title,
                        **email_data
                    )
                    alert('email', [root.get_site_sender()], [member.email],
                          subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context], context.author))
        return {}

    def after_execution(self, context, request, **kw):
        process = self.process
        proposal = process.execution_context.created_entity(
            'proposal')
        if self.sub_process:
            exec_ctx = self.sub_process.execution_context
            vote_processes = exec_ctx.get_involved_collection('vote_processes')
            opened_vote_processes = [proc for proc in vote_processes
                                     if not proc._finished]
            if opened_vote_processes:
                close_votes(proposal, request, opened_vote_processes)

        setattr(process, 'new_cycle_date', datetime.datetime.now())
        setattr(process, 'previous_alert', -1)
        super(VotingPublication, self).after_execution(proposal, request, **kw)
        is_published = publish_condition(process)
        proposal.working_group.work_duration = calculate_improvement_cycle_duration(
            process)
        if is_published:
            process.execute_action(proposal, request, 'submit', {})
        else:
            process.execute_action(proposal, request, 'work', {})

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def work_state_validation(process, context):
    return 'active' in getattr(context.working_group, 'state', []) and \
           'votes for publishing' in context.state


class Work(ElementaryAction):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'plus-action'
    style_order = 5
    context = IProposal
    processs_relation_id = 'proposal'
    #actionType = ActionType.system
    relation_validation = decision_relation_validation
    roles_validation = decision_roles_validation
    state_validation = work_state_validation

    def _send_mails(self, context, request, message_id):
        root = getSite()
        working_group = context.working_group
        duration = to_localized_time(
            calculate_improvement_cycle_date(self.process),
            translate=True)
        isclosed = 'closed' in working_group.state
        members = working_group.members
        localizer = request.localizer
        root = request.root
        #Get ballots
        vp_ballot = getattr(working_group, 'vp_ballot', '')
        wmc_ballot = getattr(working_group, 'work_mode_configuration_ballot', '')
        rc_ballot = getattr(working_group, 'reopening_configuration_ballot', '')
        dc_ballot = getattr(working_group, 'duration_configuration_ballot', '')
        # Get ballot URLs
        ballot_oid = get_oid(vp_ballot, '')
        vp_ballot_url = request.resource_url(
            root, '@@seeballot', query={'id': ballot_oid}) \
            if ballot_oid else None
        ballot_oid = get_oid(wmc_ballot, '')
        wmc_ballot_url = request.resource_url(
            root, '@@seeballot', query={'id': ballot_oid}) \
            if ballot_oid else None
        ballot_oid = get_oid(rc_ballot, '')
        rc_ballot_url = request.resource_url(
            root, '@@seeballot', query={'id': ballot_oid}) \
            if ballot_oid else None
        ballot_oid = get_oid(dc_ballot, '')
        dc_ballot_url = request.resource_url(
            root, '@@seeballot', query={'id': ballot_oid}) \
            if ballot_oid else None

        alert('internal', [root], members,
              internal_kind=InternalAlertKind.working_group_alert,
              subjects=[context], alert_kind=message_id,
              vp_ballot=vp_ballot_url,
              wmc_ballot=wmc_ballot_url,
              rc_ballot=rc_ballot_url,
              dc_ballot=dc_ballot_url)
        subject_data = get_entity_data(context, 'subject', request)
        for member in [m for m in members if getattr(m, 'email', '')]:
            mail_template = root.get_mail_template(
                message_id, member.user_locale)
            subject_template = mail_template['subject']
            message_template = mail_template['template']
            subject = subject_template.format(subject_title=context.title)
            email_data = get_user_data(member, 'recipient', request)
            email_data.update(subject_data)
            message = message_template.format(
                duration=duration,
                isclosed=localizer.translate(
                    (isclosed and _('closed')) or _('open')),
                novaideo_title=root.title,
                **email_data
            )
            alert('email', [root.get_site_sender()], [member.email],
                  subject=subject, body=message)

    def start(self, context, request, appstruct, **kw):
        working_group = context.working_group
        context.state.remove('votes for publishing')
        #Only for amendments work mode
        reopening_ballot = getattr(
            working_group, 'reopening_configuration_ballot', None)
        if reopening_ballot is not None:
            report = reopening_ballot.report
            voters_len = len(report.voters)
            electors_len = len(report.electors)
            report.calculate_votes()
            #absolute majority
            if (voters_len == electors_len) and \
               (report.result['False'] == 0) and \
               'closed' in working_group.state:
                working_group.state.remove('closed')

        context.state.insert(0, 'amendable')
        #The first improvement cycle is started
        if working_group.first_improvement_cycle:
            self._send_mails(
                context, request,
                'first_start_work')
            working_group.first_improvement_cycle = False
        else:
            self._send_mails(
                context, request,
                'start_work')

        context.reindex()
        working_group.reindex()
        request.registry.notify(ActivityExecuted(
            self, [context, working_group], context.author))
        return {}

    def after_execution(self, context, request, **kw):
        proposal = self.process.execution_context.created_entity('proposal')
        super(Work, self).after_execution(proposal, request, **kw)
        working_group = proposal.working_group
        root = request.root
        nonproductive_cycle = root.get_nonproductive_cycle_nb()
        if getattr(working_group, 'nonproductive_cycle', 1) >= nonproductive_cycle:
            end_work(proposal, request)
            proposal.state = PersistentList(
                ['open to a working group', 'published'])
            members = working_group.members
            working_group.empty(False)
            working_group.state = PersistentList(['deactivated'])
            proposal.reindex()
            working_group.reindex()
            alert(
                'internal', [request.root], members,
                internal_kind=InternalAlertKind.moderation_alert,
                subjects=[proposal], alert_kind='object_closed')
            subject_data = get_entity_data(proposal, 'subject', request)
            for member in [m for m in members if getattr(m, 'email', '')]:
                mail_template = root.get_mail_template(
                    'close_proposal', member.user_locale)
                subject = mail_template['subject'].format(
                    **subject_data)
                email_data = get_user_data(member, 'recipient', request)
                email_data.update(subject_data)
                message = mail_template['template'].format(
                    novaideo_title=root.title,
                    **email_data
                )
                alert('email', [root.get_site_sender()], [member.email],
                      subject=subject, body=message)
        else:
            self.process.execute_action(proposal, request, 'votingpublication', {})

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def submit_roles_validation(process, context):
    return has_role(role=('SiteAdmin',))


def submit_state_validation(process, context):
    wg = context.working_group
    return wg and 'active' in context.working_group.state and \
           'votes for publishing' in context.state


class SubmitProposal(ElementaryAction):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_picto = 'glyphicon glyphicon-certificate'
    style_order = 2
    context = IProposal
    processs_relation_id = 'proposal'
    #actionType = ActionType.system
    relation_validation = decision_relation_validation
    roles_validation = submit_roles_validation
    state_validation = submit_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        working_group = context.working_group
        if root.support_proposals:
            context.state = PersistentList(['submitted_support', 'published'])
            # Add Nia comment
            alert_comment_nia(
                context, request, root,
                internal_kind=InternalAlertKind.working_group_alert,
                subject_type='proposal',
                alert_kind='submitted_support',
                duplication=context
                )
        else:
            context.state = PersistentList(['published', 'submitted_support'])

        working_group.state = PersistentList(['archived'])
        working_group.setproperty('wating_list', [])
        working_group.setproperty('wating_list_participation', [])
        members = working_group.members
        for member in members:
            real_member = getattr(member, 'member', member)
            real_member.add_reserved_token(context)
            revoke_roles(member, (('Participant', context),))

        remove_ballot_processes(
            context, request.root['runtime'],
            exclude=['contentreportdecision'])
        #Alert users
        users = list(get_users_by_preferences(context))
        users.extend(members)
        users = set(users)
        #Get ballots
        vp_ballot = getattr(working_group, 'vp_ballot', '')
        # Get ballot URLs
        ballot_oid = get_oid(vp_ballot, '')
        vp_ballot_url = request.resource_url(
            root, '@@seeballot', query={'id': ballot_oid}) \
            if ballot_oid else None
        alert('internal', [root], users,
              internal_kind=InternalAlertKind.working_group_alert,
              subjects=[context], alert_kind='submit_proposal',
              ballot=vp_ballot_url)
        subject_data = get_entity_data(context, 'subject', request)
        for member in [m for m in users if getattr(m, 'email', '')]:
            mail_template = root.get_mail_template(
                'publish_proposal', member.user_locale)
            subject = mail_template['subject'].format(
                subject_title=context.title)
            email_data = get_user_data(member, 'recipient', request)
            email_data.update(subject_data)
            message = mail_template['template'].format(
                novaideo_title=root.title,
                **email_data
            )
            alert('email', [root.get_site_sender()], [member.email],
                  subject=subject, body=message)

        context.modified_at = datetime.datetime.now(tz=pytz.UTC)
        if len(members) > 1:
            alert(
                'internal', [root], members,
                internal_kind=InternalAlertKind.working_group_alert,
                subjects=[context], alert_kind='members_notation')
            alert_data = get_entity_data(context, 'subject', request)
            for member in [a for a in members if getattr(a, 'email', '')]:
                mail_template = root.get_mail_template(
                    'members_notation', member.user_locale)
                subject = mail_template['subject'].format(
                    novaideo_title=root.title,
                    **alert_data)
                email_data = get_user_data(member, 'recipient', request)
                alert_data.update(email_data)
                message = mail_template['template'].format(
                    novaideo_title=root.title,
                    **alert_data)
                alert('email', [root.get_site_sender()], [member.email],
                      subject=subject, body=message)

            for member in members:
                members_ = list(members)
                members_.remove(member)
                run_notation_process(
                    context, request, member, members_)

        working_group.reindex()
        context.reindex()
        request.registry.notify(ActivityExecuted(
            self, [context, working_group], context.author))
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def alert_relation_validation(process, context):
    return process.execution_context.has_relation(context, 'proposal')


def alert_roles_validation(process, context):
    return has_role(role=('System',))


class AlertEnd(ElementaryAction):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_order = 4
    context = IProposal
    actionType = ActionType.system
    processs_relation_id = 'proposal'
    roles_validation = alert_roles_validation
    relation_validation = alert_relation_validation

    def start(self, context, request, appstruct, **kw):
        working_group = context.working_group
        previous_alert = getattr(self.process, 'previous_alert', -1)
        setattr(self.process, 'previous_alert', previous_alert + 1)
        if 'active' in working_group.state and 'amendable' in context.state:
            members = working_group.members
            root = request.root
            alert('internal', [root], members,
                  internal_kind=InternalAlertKind.working_group_alert,
                  subjects=[context], alert_kind='alert_end_work')
            subject_data = get_entity_data(context, 'subject', request)
            for member in [m for m in members if getattr(m, 'email', '')]:
                mail_template = root.get_mail_template(
                    'alert_end', member.user_locale)
                subject = mail_template['subject'].format(
                    subject_title=context.title)
                email_data = get_user_data(member, 'recipient', request)
                email_data.update(subject_data)
                message = mail_template['template'].format(
                    novaideo_title=root.title,
                    **email_data
                )
                alert('email', [root.get_site_sender()], [member.email],
                      subject=subject, body=message)

        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


#**********************************************Workspace***************************************************


def get_access_key_ws(obj):
    return serialize_roles(
        (('Participant', obj.proposal), 'SiteAdmin', 'Admin'))


def seeworkspace_processsecurity_validation(process, context):
    return has_any_roles(
        roles=(('Participant', context.proposal), 'SiteAdmin'))


@access_action(access_key=get_access_key_ws)
class SeeWorkspace(InfiniteCardinality):
    title = _('Details')
    context = IWorkspace
    actionType = ActionType.automatic
    processsecurity_validation = seeworkspace_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def addfiles_state_validation(process, context):
    wg = context.working_group
    return wg and 'active' in wg.state and 'amendable' in context.proposal.state


class AddFiles(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-import'
    style_order = 4
    submission_title = _('Save')
    context = IWorkspace
    roles_validation = seeworkspace_processsecurity_validation
    processsecurity_validation = attach_processsecurity_validation
    state_validation = addfiles_state_validation

    def start(self, context, request, appstruct, **kw):
        add_files_to_workspace(appstruct.get('files', []), context)
        context.reindex()
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def rmfile_relation_validation(process, context):
    parent = context.__parent__
    return isinstance(parent, Workspace)


def rmfile_roles_validation(process, context):
    workspace = context.__parent__
    return has_any_roles(
        roles=(('Participant', workspace.proposal), 'SiteAdmin'))


def rmfile_state_validation(process, context):
    workspace = context.__parent__
    wg = workspace.working_group
    return wg and 'active' in wg.state and \
        'amendable' in workspace.proposal.state


class RemoveFile(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'primary-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-trash'
    style_order = 2
    submission_title = _('Continue')
    context = IFile
    roles_validation = rmfile_roles_validation
    processsecurity_validation = attach_processsecurity_validation
    state_validation = rmfile_state_validation
    relation_validation = rmfile_relation_validation

    def start(self, context, request, appstruct, **kw):
        workspace = context.__parent__
        if context in workspace.files:
            workspace.delfromproperty('files', context)

        return {'newcontext': workspace}

    def redirect(self, context, request, **kw):
        return nothing


# Proposal moderation

def decision_state_validation(process, context):
    return 'submitted' in context.state


class ModerationVote(StartBallot):
    context = IProposal
    state_validation = decision_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        moderators = self.process.execution_context.get_involved_collection(
            'electors')
        alert(
            'internal', [root], moderators,
            internal_kind=InternalAlertKind.moderation_alert,
            subjects=[context], alert_kind='moderate_content')
        subject_data = get_entity_data(context, 'subject', request)
        subject_data.update(get_user_data(context, 'subject', request))
        duration = getattr(root, 'duration_moderation_vote', 7)
        date_end = datetime.datetime.now() + \
            datetime.timedelta(days=duration)
        date_end_vote = to_localized_time(
            date_end, request, translate=True)
        subject_data['url_moderation_rules'] = request.resource_url(
            root.moderation_rules, '@@index')
        for moderator in [a for a in moderators if getattr(a, 'email', '')]:
            mail_template = root.get_mail_template(
                'moderate_content', moderator.user_locale)
            subject = mail_template['subject'].format(
                novaideo_title=root.title,
                **subject_data)
            email_data = get_user_data(moderator, 'recipient', request)
            email_data.update(subject_data)
            message = mail_template['template'].format(
                novaideo_title=root.title,
                subject_email=getattr(context, 'email', ''),
                date_end_vote=date_end_vote,
                duration=getattr(root, 'duration_moderation_vote', 7),
                **email_data)
            alert('email', [root.get_site_sender()], [moderator.email],
                  subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context], get_current()))
        return {}

    def after_execution(self, context, request, **kw):
        proposal = self.process.execution_context.involved_entity(
            'content')
        close_ballot(self, proposal, request)
        # proposal not removed
        if proposal and proposal.__parent__:
            root = getSite()
            moderators = self.process.execution_context.get_involved_collection(
                'electors')
            for moderator in moderators:
                revoke_roles(
                    user=moderator,
                    roles=(('LocalModerator', proposal),))

            ballots = getattr(self.sub_process, 'ballots', [])
            ballot = None
            for ballot_ in ballots:
                ballot_.finish_ballot()
                ballot = ballot_

            ballot_oid = get_oid(ballot, '')
            ballot_url = request.resource_url(
                root, '@@seeballot', query={'id': ballot_oid}) \
                if ballot_oid else None
            accepted = ballot_result(self, _marker)
            user = get_current()
            if accepted:
                not_published_ideas = publish_proposal_moderation(
                    proposal, request, root,
                    ballot_url=ballot_url if accepted is not _marker else None)
                request.registry.notify(ActivityExecuted(
                    self, not_published_ideas, user))
            else:
                archive_proposal_moderation(
                    proposal, request, root, {'explanation': ''},
                    ballot_url=ballot_url)

        super(ModerationVote, self).after_execution(
            proposal, request, **kw)

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


# Proposal participation

class ParticipationVote(StartBallot):
    context = IProposal
    state_validation = participate_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        participant = self.process.participant
        moderators = self.process.execution_context.get_involved_collection(
            'electors')
        alert_data = get_entity_data(participant, 'participant', request)
        alert(
            'internal', [root], moderators,
            internal_kind=InternalAlertKind.working_group_alert,
            subjects=[context], alert_kind='new_participant',
            **alert_data)
        subject_data = get_entity_data(context, 'subject', request)
        subject_data.update(get_user_data(participant, 'user', request))
        duration = getattr(root, 'duration_moderation_vote', 7)
        date_end = datetime.datetime.now() + \
            datetime.timedelta(days=duration)
        date_end_vote = to_localized_time(
            date_end, request, translate=True)
        for moderator in [a for a in moderators if getattr(a, 'email', '')]:
            mail_template = root.get_mail_template(
                'new_participant', moderator.user_locale)
            subject = mail_template['subject'].format(
                novaideo_title=root.title,
                **subject_data)
            email_data = get_user_data(moderator, 'recipient', request)
            email_data.update(subject_data)
            message = mail_template['template'].format(
                novaideo_title=root.title,
                subject_email=getattr(context, 'email', ''),
                date_end_vote=date_end_vote,
                duration=duration,
                **email_data)
            alert('email', [root.get_site_sender()], [moderator.email],
                  subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context], get_current()))
        return {}

    def after_execution(self, context, request, **kw):
        proposal = self.process.execution_context.involved_entity(
            'content')
        close_ballot(self, proposal, request)
        # proposal not removed
        if proposal and proposal.__parent__:
            root = getSite()
            participant = self.process.participant
            participant_data = get_entity_data(
                participant, 'participant', request)
            ballots = getattr(self.sub_process, 'ballots', [])
            period_date = None
            ballot = None
            if ballots:
                ballot = ballots[0]
                period_date = datetime.datetime.now(tz=pytz.UTC) + \
                    ballot.period_validity

            ballot_oid = get_oid(ballot, '')
            ballot_url = request.resource_url(
                root, '@@seeballot', query={'id': ballot_oid})
            accepted = ballot_result(self)
            working_group = proposal.working_group
            members = working_group.members
            if accepted:
                wgs = getattr(participant, 'active_working_groups', [])
                if len(wgs) < root.participations_maxi:
                    accept_participation(
                        proposal, request, participant, root,
                        ballot_url=ballot_url)
                    request.registry.notify(ActivityExecuted(
                        self, [proposal, proposal.working_group], participant))
                else:
                    working_group.delfromproperty(
                        'wating_list_participation', participant)
                    alert(
                        'internal', [root], [participant],
                        internal_kind=InternalAlertKind.working_group_alert,
                        subjects=[proposal], alert_kind='cancel_participation')
                    alert(
                        'internal', [root], members,
                        internal_kind=InternalAlertKind.working_group_alert,
                        subjects=[proposal],
                        alert_kind='cancel_participation_members',
                        **participant_data)
            else:
                working_group.delfromproperty(
                    'wating_list_participation', participant)
                alert(
                    'internal', [root], [participant],
                    internal_kind=InternalAlertKind.working_group_alert,
                    subjects=[proposal], alert_kind='refuse_participant',
                    period_date=period_date,
                    ballot=ballot_url)
                alert(
                    'internal', [root], members,
                    internal_kind=InternalAlertKind.working_group_alert,
                    subjects=[proposal],
                    alert_kind='refuse_participant_members',
                    period_date=period_date,
                    ballot=ballot_url,
                    **participant_data)

        super(ParticipationVote, self).after_execution(
            proposal, request, **kw)

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


# Exclude a participant

class ExclusionVote(StartBallot):
    context = IProposal
    state_validation = exclude_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        participant = self.process.participant
        moderators = self.process.execution_context.get_involved_collection(
            'electors')
        alert_data = get_entity_data(participant, 'participant', request)
        alert(
            'internal', [root], moderators,
            internal_kind=InternalAlertKind.working_group_alert,
            subjects=[context], alert_kind='exclude_participant',
            **alert_data)
        subject_data = get_entity_data(context, 'subject', request)
        subject_data.update(get_user_data(participant, 'user', request))
        duration = getattr(root, 'duration_moderation_vote', 7)
        date_end = datetime.datetime.now() + \
            datetime.timedelta(days=duration)
        date_end_vote = to_localized_time(
            date_end, request, translate=True)
        for moderator in [a for a in moderators if getattr(a, 'email', '')]:
            mail_template = root.get_mail_template(
                'exclude_participant', moderator.user_locale)
            subject = mail_template['subject'].format(
                novaideo_title=root.title,
                **subject_data)
            email_data = get_user_data(moderator, 'recipient', request)
            email_data.update(subject_data)
            message = mail_template['template'].format(
                novaideo_title=root.title,
                subject_email=getattr(context, 'email', ''),
                date_end_vote=date_end_vote,
                duration=duration,
                **email_data)
            alert('email', [root.get_site_sender()], [moderator.email],
                  subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context], get_current()))
        return {}

    def after_execution(self, context, request, **kw):
        proposal = self.process.execution_context.involved_entity(
            'content')
        close_ballot(self, proposal, request)
        # proposal not removed
        if proposal and proposal.__parent__:
            root = getSite()
            participant = self.process.participant
            ballots = getattr(self.sub_process, 'ballots', [])
            period_date = None
            ballot = None
            if ballots:
                ballot = ballots[0]
                period_date = datetime.datetime.now(tz=pytz.UTC) + \
                    ballot.period_validity

            ballot_oid = get_oid(ballot, '')
            ballot_url = request.resource_url(
                root, '@@seeballot', query={'id': ballot_oid})
            accepted = ballot_result(self)
            if accepted:
                exclude_participant_from_wg(
                    proposal, request, participant, root, 'exclude',
                    period_date=period_date,
                    ballot_url=ballot_url)
            else:
                participant_data = get_entity_data(
                    participant, 'participant', request)
                members = proposal.working_group.members
                alert(
                    'internal', [root], [participant],
                    internal_kind=InternalAlertKind.working_group_alert,
                    subjects=[proposal], alert_kind='refuse_exclusion',
                    period_date=period_date,
                    ballot=ballot_url)
                alert(
                    'internal', [root], members,
                    internal_kind=InternalAlertKind.working_group_alert,
                    subjects=[proposal],
                    alert_kind='refuse_exclusion_members',
                    period_date=period_date,
                    ballot=ballot_url,
                    **participant_data)

        super(ExclusionVote, self).after_execution(
            proposal, request, **kw)

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))

#TODO behaviors

VALIDATOR_BY_CONTEXT[Proposal] = {
    'action': CommentProposal,
    'see': SeeProposal,
    'access_key': get_access_key
}
