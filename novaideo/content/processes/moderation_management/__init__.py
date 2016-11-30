# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

from novaideo.content.processes.ballot_processes import close_votes

from dace.util import (
    find_service as dace_find_service)
from dace.objectofcollaboration.principal.util import grant_roles

from novaideo import _
from novaideo.utilities.alerts_utility import (
    alert, get_user_data, get_entity_data)
from novaideo.mail import MODERATOR_DATA


MODERATORS_NB = 3


MODERATION_DATA = {
    'default': {
        'ballot_description': _("Moderation"),
        'ballot_title': _("Moderation"),
        'true_value': _("Favor"),
        'false_value': _("Against"),
        'process_id': None
    }
}


def get_moderation_data_by_type(context, process_id):
    id_ = context.__class__.__name__ + '-' + process_id
    return MODERATION_DATA.get(id_, MODERATION_DATA['default'])


def close_ballot(action, context, request):
    if action.sub_process:
        exec_ctx = action.sub_process.execution_context
        vote_processes = exec_ctx.get_involved_collection(
            'vote_processes')
        opened_vote_processes = [process for process in vote_processes
                                 if not process._finished]
        if opened_vote_processes:
            close_votes(context, request, opened_vote_processes)


def start_moderation_proc(context, process_id):
    def_container = dace_find_service('process_definition_container')
    runtime = dace_find_service('runtime')
    proc = None
    if process_id:
        pd = def_container.get_definition(process_id)
        proc = pd()
        proc.__name__ = proc.id
        runtime.addtoproperty('processes', proc)
        proc.defineGraph(pd)
        proc.execution_context.add_created_entity(
            'content', context)
        proc.execute()

    return proc


def moderation_result(process):
    context = process.execution_context.created_entity(
        'content')
    if context:
        report = context.moderation_ballot.report
        report.calculate_votes()
        if not report.voters:
            return False

        electeds = report.get_electeds()
        if electeds is None:
            return False
        else:
            return True

    return False


def start_moderation(
    context, author, request,
    root, mail_id, moderators, process_id):
    email_data = get_user_data(
        author, 'recipient', request)
    email_data.update(get_entity_data(context, 'subject', request))
    moderators_str = ""
    for index, moderator in enumerate(moderators):
        moderator_data = get_user_data(
            moderator, 'subject', request)
        moderator_data['subject_email'] = moderator.email
        moderator_data['index'] = str(index+1)
        moderator_str = MODERATOR_DATA.format(
            **moderator_data)
        moderators_str += "\n" + moderator_str
        grant_roles(
            user=moderator,
            roles=(('LocalModerator', context),))

    email_data['moderators'] = moderators_str
    context.setproperty('moderators', moderators)
    # send an email to user
    mail_template = root.get_mail_template(mail_id)
    subject = mail_template['subject'].format(
        novaideo_title=root.title)
    message = mail_template['template'].format(
        duration=getattr(root, 'duration_moderation_vote', 7),
        novaideo_title=root.title,
        **email_data)
    alert('email', [root.get_site_sender()], [author.email],
          subject=subject, body=message)
    # start a moderation process
    moderation_proc = start_moderation_proc(
        context, process_id)
    if moderation_proc:
        context.setproperty(
            'moderation_proc', moderation_proc)
        moderation_proc.execute_action(
            context, request, 'moderation_vote', {})
