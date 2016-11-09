# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

import colander
import transaction
import datetime
import pytz
from persistent.list import PersistentList
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.threadlocal import get_current_request

from substanced.util import get_oid
from substanced.event import LoggedIn
from substanced.util import find_service

from dace.util import (
    getSite, name_chooser,
    push_callback_after_commit, get_socket,
    find_service as dace_find_service)
from dace.objectofcollaboration.principal.role import DACE_ROLES
from dace.objectofcollaboration.principal.util import (
    grant_roles,
    has_role,
    get_current,
    has_any_roles,
    revoke_roles,
    get_roles,
    Anonymous,
    get_users_with_role)
from dace.processinstance.activity import (
    InfiniteCardinality,
    ElementaryAction,
    ActionType)
from dace.processinstance.core import ActivityExecuted, PROCESS_HISTORY_KEY

from ..comment_management import VALIDATOR_BY_CONTEXT
from novaideo.content.interface import (
    INovaIdeoApplication, IPerson, IPreregistration)
from novaideo.content.token import Token
from novaideo.content.person import (
    Person, PersonSchema, DEADLINE_PREREGISTRATION)
from novaideo.utilities.util import (
    to_localized_time, gen_random_token, connect)
from novaideo import _, nothing
from novaideo.core import (
    access_action, serialize_roles, PrivateChannel)
from novaideo.views.filter import (
    get_users_by_preferences, get_random_users)
from novaideo.content.alert import InternalAlertKind
from novaideo.utilities.alerts_utility import (
    alert, get_user_data, get_entity_data)
from novaideo.content.novaideo_application import NovaIdeoApplication
from novaideo.content.processes import global_user_processsecurity
from novaideo.role import get_authorized_roles
from novaideo.content.processes.ballot_processes import close_votes


MODERATORS_NB = 3


def close_ballot(action, preregistration, request):
    if action.sub_process:
        exec_ctx = action.sub_process.execution_context
        vote_processes = exec_ctx.get_involved_collection(
            'vote_processes')
        opened_vote_processes = [process for process in vote_processes
                                 if not process._finished]
        if opened_vote_processes:
            close_votes(preregistration, request, opened_vote_processes)


def start_moderation_proc(preregistration):
    def_container = dace_find_service('process_definition_container')
    runtime = dace_find_service('runtime')
    pd = def_container.get_definition('registrationmoderation')
    proc = pd()
    proc.__name__ = proc.id
    runtime.addtoproperty('processes', proc)
    proc.defineGraph(pd)
    proc.execution_context.add_created_entity(
        'preregistration', preregistration)
    proc.execute()
    return proc


def moderation_result(process):
    preregistration = process.execution_context.created_entity(
        'preregistration')
    if preregistration:
        report = preregistration.moderation_ballot.report
        report.calculate_votes()
        if not report.voters:
            return False

        electeds = report.get_electeds()
        if electeds is None:
            return False
        else:
            return True

    return False


def accept_preregistration(request, preregistration, root):
    if getattr(preregistration, 'email', ''):
        deadline_date = preregistration.get_deadline_date()
        url = request.resource_url(preregistration, "")
        mail_template = root.get_mail_template('preregistration')
        recipientdata = get_user_data(preregistration, 'recipient', request)
        subject = mail_template['subject'].format(
            novaideo_title=root.title)
        deadline_str = to_localized_time(
            deadline_date, request, translate=True)
        message = mail_template['template'].format(
            url=url,
            deadline_date=deadline_str.lower(),
            novaideo_title=root.title,
            **recipientdata)
        alert('email', [root.get_site_sender()], [preregistration.email],
              subject=subject, body=message)


def initialize_tokens(person, tokens_nb):
    for i in range(tokens_nb):
        token = Token(title='Token_'+str(i))
        person.addtoproperty('tokens_ref', token)
        person.addtoproperty('tokens', token)
        token.setproperty('owner', person)


def access_user_processsecurity(process, context):
    request = get_current_request()
    return request.accessible_to_anonymous


def login_roles_validation(process, context):
    return has_any_roles(roles=('Anonymous', 'Collaborator'))


class LogIn(InfiniteCardinality):
    title = _('Log in')
    access_controled = True
    context = INovaIdeoApplication
    roles_validation = login_roles_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        root = getSite()
        return HTTPFound(request.resource_url(root))


def logout_roles_validation(process, context):
    return has_role(role=('Collaborator',))


class LogOut(InfiniteCardinality):
    title = _('Log out')
    access_controled = True
    context = INovaIdeoApplication
    roles_validation = logout_roles_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        root = getSite()
        return HTTPFound(request.resource_url(root))


def edit_roles_validation(process, context):
    return has_any_roles(roles=(('Owner', context), 'SiteAdmin'))


def edit_processsecurity_validation(process, context):
    return global_user_processsecurity()


def edit_state_validation(process, context):
    return 'active' in context.state


class Edit(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'text-action'
    style_picto = 'glyphicon glyphicon-pencil'
    style_order = 1
    title = _('Edit')
    submission_title = _('Save')
    context = IPerson
    roles_validation = edit_roles_validation
    processsecurity_validation = edit_processsecurity_validation
    state_validation = edit_state_validation

    def start(self, context, request, appstruct, **kw):
        organization = appstruct.get('organization', None)
        changepassword = appstruct['change_password']['changepassword']
        current_user_password = appstruct['change_password']['currentuserpassword']
        user = get_current()
        if changepassword and user.check_password(current_user_password):
            password = appstruct['change_password']['password']
            context.set_password(password)

        root = getSite()
        root.merge_tree(context.tree)
        context.set_title()
        context.set_organization(organization)
        context.modified_at = datetime.datetime.now(tz=pytz.UTC)
        context.reindex()
        request.registry.notify(ActivityExecuted(self, [context], user))
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def deactivate_roles_validation(process, context):
    return (context.organization and \
            has_role(role=('OrganizationResponsible',
                           context.organization))) or \
            has_role(role=('SiteAdmin',))


def deactivate_processsecurity_validation(process, context):
    return global_user_processsecurity()


def deactivate_state_validation(process, context):
    return 'active' in context.state


class Deactivate(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'plus-action'
    style_picto = 'glyphicon glyphicon-ban-circle'
    style_order = 0
    title = _('Deactivate the profile')
    context = IPerson
    roles_validation = deactivate_roles_validation
    processsecurity_validation = deactivate_processsecurity_validation
    state_validation = deactivate_state_validation

    def start(self, context, request, appstruct, **kw):
        context.state.remove('active')
        context.state.append('deactivated')
        context.modified_at = datetime.datetime.now(tz=pytz.UTC)
        context.reindex()
        pref_author = list(get_users_by_preferences(context))
        alert('internal', [request.root], pref_author,
              internal_kind=InternalAlertKind.content_alert,
              subjects=[context], alert_kind='user_deactivated')
        request.registry.notify(ActivityExecuted(
            self, [context], get_current()))
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def activate_roles_validation(process, context):
    return (context.organization and \
            has_role(role=('OrganizationResponsible',
                           context.organization))) or \
            has_role(role=('SiteAdmin',))


def activate_processsecurity_validation(process, context):
    return global_user_processsecurity()


def activate_state_validation(process, context):
    return 'deactivated' in context.state


class Activate(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'plus-action'
    style_picto = 'glyphicon glyphicon-ok-circle'
    style_order = 0
    title = _('Activate the profile')
    context = IPerson
    roles_validation = activate_roles_validation
    processsecurity_validation = activate_processsecurity_validation
    state_validation = activate_state_validation

    def start(self, context, request, appstruct, **kw):
        context.state.remove('deactivated')
        context.state.append('active')
        context.modified_at = datetime.datetime.now(tz=pytz.UTC)
        context.reindex()
        request.registry.notify(ActivityExecuted(
            self, [context], get_current()))
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def assignroles_roles_validation(process, context):
    return has_role(role=('SiteAdmin', ))


def assignroles_processsecurity_validation(process, context):
    return global_user_processsecurity()


def assignroles_state_validation(process, context):
    return 'active' in context.state


class AssignRoles(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'text-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-tower'
    style_order = 2
    title = _('Assign roles')
    submission_title = _('Save')
    context = IPerson
    roles_validation = assignroles_roles_validation
    processsecurity_validation = assignroles_processsecurity_validation
    state_validation = assignroles_state_validation

    def start(self, context, request, appstruct, **kw):
        new_roles = list(appstruct['roles'])
        authorized_roles = get_authorized_roles()
        new_roles = [r for r in new_roles if r in authorized_roles]
        if new_roles:
            current_roles = [r for r in get_roles(context) if
                             not getattr(
                                 DACE_ROLES.get(r, None), 'islocal', False)]
            roles_to_revoke = [r for r in current_roles
                               if r not in new_roles]
            roles_to_grant = [r for r in new_roles
                              if r not in current_roles]
            revoke_roles(context, roles_to_revoke)
            grant_roles(context, roles_to_grant)
            context.modified_at = datetime.datetime.now(tz=pytz.UTC)
            context.reindex()
            request.registry.notify(ActivityExecuted(
                self, [context], get_current()))

        return {}

    def redirect(self, context, request, **kw):
        return nothing


def get_access_key(obj):
    return ['always']


def seeperson_processsecurity_validation(process, context):
    return access_user_processsecurity(process, context)#'active' in context.state


@access_action(access_key=get_access_key)
class SeePerson(InfiniteCardinality):
    # style = 'button' #TODO add style abstract class
    # style_descriminator = 'access-action'
    # style_interaction = 'ajax-action'
    # style_interaction_type = 'sidebar'
    # style_picto = 'glyphicon glyphicon-eye-open'
    title = _('Details')
    context = IPerson
    actionType = ActionType.automatic
    processsecurity_validation = seeperson_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def reg_roles_validation(process, context):
    return has_role(role=('Anonymous',))


def reg_processsecurity_validation(process, context):
    root = getSite()
    return not getattr(root, 'only_invitation', False)


def remove_expired_preregistration(root, preregistration):
    if preregistration.__parent__ is not None:
        oid = str(get_oid(preregistration))
        root.delfromproperty('preregistrations', preregistration)
        get_socket().send_pyobj(
            ('ack', 'persistent_' + oid))


class Registration(InfiniteCardinality):
    submission_title = _('Save')
    context = INovaIdeoApplication
    roles_validation = reg_roles_validation
    processsecurity_validation = reg_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        preregistration = appstruct['_object_data']
        preregistration.__name__ = gen_random_token()
        root = getSite()
        root.addtoproperty('preregistrations', preregistration)
        deadline = DEADLINE_PREREGISTRATION * 1000
        call_id = 'persistent_' + str(get_oid(preregistration))
        push_callback_after_commit(
            remove_expired_preregistration, deadline, call_id,
            root=root, preregistration=preregistration)
        preregistration.state.append('pending')
        preregistration.reindex()
        transaction.commit()
        if not getattr(root, 'moderate_registration', False):
            accept_preregistration(request, preregistration, root)
        else:
            moderators = get_random_users(MODERATORS_NB)
            for moderator in moderators:
                grant_roles(
                    user=moderator,
                    roles=(('LocalModerator', preregistration),))

            preregistration.setproperty('moderators', moderators)
            moderation_proc = start_moderation_proc(
                preregistration)
            preregistration.setproperty(
                'moderation_proc', moderation_proc)
            moderation_proc.execute_action(
                preregistration, request, 'moderation_vote', {})

        request.registry.notify(ActivityExecuted(self, [preregistration], None))
        return {'preregistration': preregistration}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(
            context, "@@registrationsubmitted"))


def confirm_processsecurity_validation(process, context):
    return not context.is_expired


def confirm_state_validation(process, context):
    root = getSite()
    if getattr(root, 'moderate_registration', False):
        return 'accepted' in context.state

    return True


class ConfirmRegistration(InfiniteCardinality):
    submission_title = _('Save')
    context = IPreregistration
    roles_validation = reg_roles_validation
    processsecurity_validation = confirm_processsecurity_validation
    state_validation = confirm_state_validation

    def start(self, context, request, appstruct, **kw):
        data = context.get_data(PersonSchema())
        data['Keep_me_anonymous'] = getattr(context, 'Keep_me_anonymous', False)
        data['pseudonym'] = getattr(context, 'pseudonym', None)
        annotations = getattr(context, 'annotations', {}).get(
            PROCESS_HISTORY_KEY, [])
        data.update({'password': appstruct['password']})
        data = {key: value for key, value in data.items()
                if value is not colander.null}
        data.pop('title')
        root = getSite()
        person = Person(**data)
        principals = find_service(root, 'principals')
        name = person.first_name + ' ' + person.last_name \
            if not getattr(person, 'Keep_me_anonymous', False) else \
            person.pseudonym
        users = principals['users']
        name = name_chooser(users, name=name)
        users[name] = person
        grant_roles(person, roles=('Member',))
        grant_roles(person, (('Owner', person),))
        person.state.append('active')
        initialize_tokens(person, root.tokens_mini)
        get_socket().send_pyobj(
            ('stop',
             'persistent_' + str(get_oid(context))))
        root.delfromproperty('preregistrations', context)
        person.init_annotations()
        person.annotations.setdefault(
            PROCESS_HISTORY_KEY, PersistentList()).extend(annotations)
        person.reindex()
        request.registry.notify(ActivityExecuted(self, [person], person))
        root.addtoproperty('news_letter_members', person)
        newsletters = root.get_newsletters_automatic_registration()
        email = getattr(person, 'email', '')
        if newsletters and email:
            for newsletter in newsletters:
                newsletter.subscribe(
                    person.first_name, person.last_name, email)

        transaction.commit()
        if email:
            mail_template = root.get_mail_template('registration_confiramtion')
            subject = mail_template['subject'].format(
                novaideo_title=root.title)
            recipientdata = get_user_data(person, 'recipient', request)
            message = mail_template['template'].format(
                login_url=request.resource_url(root, '@@login'),
                novaideo_title=root.title,
                **recipientdata)
            alert('email', [root.get_site_sender()], [email],
                  subject=subject, body=message)

        return {'person': person}

    def redirect(self, context, request, **kw):
        person = kw['person']
        headers = remember(request, get_oid(person))
        request.registry.notify(LoggedIn(person.email, person,
                                         context, request))
        return HTTPFound(location=request.resource_url(context),
                         headers=headers)


def remind_roles_validation(process, context):
    organization = getattr(context, 'organization', None)
    if organization:
        return has_any_roles(
            roles=('SiteAdmin', ('OrganizationResponsible', organization)))

    return has_role(role=('SiteAdmin',))


def remind_processsecurity_validation(process, context):
    return getattr(context, 'email', '') and \
        global_user_processsecurity()


def remind_state_validation(process, context):
    root = getSite()
    moderate_registration = getattr(root, 'moderate_registration', False)
    if moderate_registration:
        return 'accepted' in context.state

    return True


class Remind(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-refresh'
    style_order = 3
    context = IPreregistration
    submission_title = _('Continue')
    state_validation = remind_state_validation
    roles_validation = remind_roles_validation
    processsecurity_validation = remind_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        root = request.root
        url = request.resource_url(context, "")
        deadline_date = context.init_deadline(
            datetime.datetime.now(tz=pytz.UTC))
        deadline_str = to_localized_time(
            deadline_date, request, translate=True)
        mail_template = root.get_mail_template('preregistration')
        recipientdata = get_user_data(context, 'recipient', request)
        subject = mail_template['subject'].format(
            novaideo_title=root.title)
        deadline_str = to_localized_time(
            deadline_date, request, translate=True)
        message = mail_template['template'].format(
            url=url,
            deadline_date=deadline_str.lower(),
            novaideo_title=root.title,
            **recipientdata)
        alert('email', [root.get_site_sender()], [context.email],
              subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context], get_current()))
        return {}

    def redirect(self, context, request, **kw):
        return nothing


def get_access_key_reg(obj):
    organization = getattr(obj, 'organization', None)
    if organization:
        return serialize_roles(
            ('SiteAdmin', 'Admin',
             ('OrganizationResponsible', obj),
             ('LocalModerator', obj)))

    return serialize_roles(('SiteAdmin', 'Admin', ('LocalModerator', obj)))


def seereg_processsecurity_validation(process, context):
    has_role_cond = False
    organization = getattr(context, 'organization', None)
    if organization:
        has_role_cond = has_any_roles(
            roles=('SiteAdmin',
                   ('OrganizationResponsible', context),
                   ('LocalModerator', context)))
    else:
        has_role_cond = has_any_roles(
            roles=('SiteAdmin', ('LocalModerator', context)))

    return has_role_cond and \
        global_user_processsecurity()


@access_action(access_key=get_access_key_reg)
class SeeRegistration(InfiniteCardinality):
    title = _('Details')
    context = IPreregistration
    actionType = ActionType.automatic
    processsecurity_validation = seereg_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def seeregs_processsecurity_validation(process, context):
    return has_any_roles(
        roles=('SiteAdmin', 'OrganizationResponsible', 'LocalModerator')) and \
        global_user_processsecurity()


class SeeRegistrations(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'admin-action'
    style_picto = 'typcn typcn-user-add'
    style_order = 4
    isSequential = False
    context = INovaIdeoApplication
    processsecurity_validation = seeregs_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context))


def remove_processsecurity_validation(process, context):
    return has_any_roles(roles=('SiteAdmin', 'OrganizationResponsible')) and \
           global_user_processsecurity()


class RemoveRegistration(InfiniteCardinality):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'global-action'
    style_interaction = 'ajax-action'
    style_picto = 'glyphicon glyphicon-trash'
    style_order = 5
    submission_title = _('Remove')
    context = IPreregistration
    processsecurity_validation = remove_processsecurity_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        for moderator in context.moderators:
            revoke_roles(user=moderator, roles=(('LocalModerator', context),))

        if context.moderation_proc:
            vote_actions = context.moderation_proc.get_actions(
                'moderation_vote')
            if vote_actions:
                action = vote_actions[0]
                close_ballot(action, context, request)

        root.delfromproperty('preregistrations', context)
        return {'root': root}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, '@@seeregistrations'))


def discuss_roles_validation(process, context):
    return has_role(role=('Member',))


def discuss_processsecurity_validation(process, context):
    user = get_current()
    return context is not user and \
        global_user_processsecurity()


def discuss_state_validation(process, context):
    return 'active' in context.state


class Discuss(InfiniteCardinality):
    isSequential = False
    style_descriminator = 'communication-action'
    style_interaction = 'ajax-action'
    style_interaction_type = 'sidebar'
    style_interaction_args = 'scroll-bottom'
    style_picto = 'ion-chatbubble'
    style_order = 0
    style_activate = True
    context = IPerson
    roles_validation = discuss_roles_validation
    processsecurity_validation = discuss_processsecurity_validation
    state_validation = discuss_state_validation

    def get_nb(self, context, request):
        user = get_current()
        channel = context.get_channel(user)
        if channel:
            unread_comments = channel.get_comments_between(
                user.get_read_date(channel),
                datetime.datetime.now(tz=pytz.UTC))
            return len(unread_comments)

        return 0

    def get_title(self, context, request):
        user = get_current()
        channel = context.get_channel(user)
        len_comments = channel.len_comments if channel else 0
        return _("${title} (${nember})",
                 mapping={'nember': len_comments,
                          'title': request.localizer.translate(self.title)})

    def _get_users_to_alerts(self, context, request, user, channel):
        users = list(channel.members)
        if user in users:
            users.remove(user)

        return users

    def _alert_users(self, context, request, user, comment, channel):
        root = getSite()
        users = self._get_users_to_alerts(context, request, user, channel)
        mail_template = root.get_mail_template('alert_discuss')
        author_data = get_user_data(user, 'author', request)
        alert_data = get_entity_data(comment, 'comment', request)
        alert_data.update(author_data)
        alert('internal', [root], users,
              internal_kind=InternalAlertKind.comment_alert,
              subjects=[channel],
              comment_kind='discuss',
              **alert_data)
        subject_data = get_entity_data(user, 'subject', request)
        alert_data.update(subject_data)
        subject = mail_template['subject'].format(
            **subject_data)
        for user_to_alert in [u for u in users if getattr(u, 'email', '')]:
            email_data = get_user_data(user_to_alert, 'recipient', request)
            email_data.update(alert_data)
            message = mail_template['template'].format(
                novaideo_title=root.title,
                **email_data
            )
            alert('email', [root.get_site_sender()], [user_to_alert.email],
                  subject=subject, body=message)

    def start(self, context, request, appstruct, **kw):
        comment = appstruct['_object_data']
        user = get_current()
        channel = context.get_channel(user)
        if not channel:
            channel = PrivateChannel()
            context.addtoproperty('channels', channel)
            channel.addtoproperty('members', user)
            channel.addtoproperty('members', context)
            context.set_read_date(channel, comment.created_at)

        if channel:
            channel.addtoproperty('comments', comment)
            channel.add_comment(comment)
            comment.format(request)
            comment.setproperty('author', user)
            grant_roles(user=user, roles=(('Owner', comment), ))
            if appstruct['related_contents']:
                related_contents = appstruct['related_contents']
                correlation = connect(
                    context,
                    list(related_contents),
                    {'comment': comment.comment,
                     'type': comment.intention},
                    user,
                    unique=True)
                comment.setproperty('related_correlation', correlation[0])

            self._alert_users(context, request, user, comment, channel)
            context.reindex()
            user.set_read_date(channel, datetime.datetime.now(tz=pytz.UTC))

        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


def gdiscuss_processsecurity_validation(process, context):
    return global_user_processsecurity()


class GeneralDiscuss(InfiniteCardinality):
    isSequential = False
    style_interaction = 'ajax-action'
    style_interaction_type = 'sidebar'
    style_interaction_args = 'scroll-bottom'
    style_picto = 'ion-chatbubble'
    style_order = 0
    style_activate = True
    context = INovaIdeoApplication
    roles_validation = discuss_roles_validation
    processsecurity_validation = gdiscuss_processsecurity_validation

    def get_nb(self, context, request):
        channel = context.channel
        if channel:
            user = get_current()
            if hasattr(user, 'get_read_date'):
                unread_comments = channel.get_comments_between(
                    user.get_read_date(channel),
                    datetime.datetime.now(tz=pytz.UTC))
                return len(unread_comments)

        return 0

    def _get_users_to_alerts(self, context, request, user, channel):
        return 'all'

    def _alert_users(self, context, request, user, comment, channel):
        root = getSite()
        users = self._get_users_to_alerts(context, request, user, channel)
        comment_oid = getattr(comment, '__oid__', 'None')
        authordata = get_user_data(user, 'author', request)
        alert('internal', [root], users, exclude=[user],
              internal_kind=InternalAlertKind.comment_alert,
              subjects=[channel],
              comment_oid=comment_oid,
              comment_content=comment.comment,
              comment_kind='general_discuss',
              **authordata)

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        comment = appstruct['_object_data']
        user = get_current()
        channel = root.channel
        #TODO get
        if channel:
            channel.addtoproperty('comments', comment)
            channel.add_comment(comment)
            comment.format(request)
            comment.setproperty('author', user)
            grant_roles(user=user, roles=(('Owner', comment), ))
            if appstruct['related_contents']:
                related_contents = appstruct['related_contents']
                correlation = connect(
                    context,
                    list(related_contents),
                    {'comment': comment.comment,
                     'type': comment.intention},
                    user,
                    unique=True)
                comment.setproperty('related_correlation', correlation[0])

            self._alert_users(context, request, user, comment, channel)
            context.reindex()
            user.set_read_date(channel, datetime.datetime.now(tz=pytz.UTC))

        return {}

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


# Registration moderation

def decision_relation_validation(process, context):
    return process.execution_context.has_relation(context, 'preregistration')


def decision_roles_validation(process, context):
    return has_role(role=('SiteAdmin',))


def decision_state_validation(process, context):
    return 'pending' in context.state


class ModerationVote(ElementaryAction):
    style = 'button' #TODO add style abstract class
    style_descriminator = 'plus-action'
    style_order = 5
    context = IPreregistration
    processs_relation_id = 'preregistration'
    #actionType = ActionType.system
    relation_validation = decision_relation_validation
    roles_validation = decision_roles_validation
    state_validation = decision_state_validation

    def start(self, context, request, appstruct, **kw):
        root = getSite()
        moderators = context.moderators
        alert(
            'internal', [root], moderators,
            internal_kind=InternalAlertKind.admin_alert,
            subjects=[context], alert_kind='new_registration')
        mail_template = root.get_mail_template('moderate_preregistration')
        subject = mail_template['subject'].format(
            novaideo_title=root.title)
        url = request.resource_url(context, '@@index')
        subject_data = get_user_data(context, 'subject', request)
        for moderator in [a for a in moderators if getattr(a, 'email', '')]:
            email_data = get_user_data(moderator, 'recipient', request)
            email_data.update(subject_data)
            message = mail_template['template'].format(
                url=url,
                novaideo_title=root.title,
                subject_email=getattr(context, 'email', ''),
                duration=getattr(root, 'duration_moderation_vote', 1),
                **email_data)
            alert('email', [root.get_site_sender()], [moderator.email],
                  subject=subject, body=message)

        request.registry.notify(ActivityExecuted(
            self, [context], get_current()))
        return {}

    def after_execution(self, context, request, **kw):
        preregistration = self.process.execution_context.created_entity(
            'preregistration')
        close_ballot(self, preregistration, request)
        # preregistration not removed
        if preregistration and preregistration.__parent__:
            for moderator in preregistration.moderators:
                revoke_roles(
                    user=moderator,
                    roles=(('LocalModerator', preregistration),))

            accepted = moderation_result(self.process)
            root = getSite()
            if accepted:
                preregistration.state = PersistentList(['accepted'])
                accept_preregistration(request, preregistration, root)
                preregistration.reindex()
            else:
                mail_template = root.get_mail_template(
                    'moderate_preregistration_refused')
                subject = mail_template['subject'].format(
                    novaideo_title=root.title)
                email_data = get_user_data(
                    preregistration, 'recipient', request)
                message = mail_template['template'].format(
                    novaideo_title=root.title,
                    **email_data)
                alert(
                    'email', [root.get_site_sender()],
                    [preregistration.email],
                    subject=subject, body=message)
                remove_expired_preregistration(root, preregistration)

        super(ModerationVote, self).after_execution(
            preregistration, request, **kw)

    def redirect(self, context, request, **kw):
        return HTTPFound(request.resource_url(context, "@@index"))


#TODO behaviors

VALIDATOR_BY_CONTEXT[Person] = Discuss

VALIDATOR_BY_CONTEXT[NovaIdeoApplication] = GeneralDiscuss
