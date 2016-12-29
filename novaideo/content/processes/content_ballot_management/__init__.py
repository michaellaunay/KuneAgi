# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

import datetime

from dace.util import (
    find_service as dace_find_service)
from dace.objectofcollaboration.principal.util import grant_roles

from novaideo.content.processes.ballot_processes import close_votes
from novaideo import _
from novaideo.utilities.alerts_utility import (
    alert, get_user_data, get_entity_data)
from novaideo.utilities.util import to_localized_time
from novaideo.mail import MODERATOR_DATA


ELECTORS_NB = 3


BALLOT_DATA = {
    'default': {
        'ballot_description': _("Moderation"),
        'ballot_title': _("Moderation"),
        'true_value': _("Favor"),
        'false_value': _("Against"),
        'process_id': None
    }
}


def get_ballot_data_by_type(context, process_id):
    id_ = context.__class__.__name__ + '-' + process_id
    return BALLOT_DATA.get(id_, BALLOT_DATA['default'])


def close_ballot(action, context, request):
    if action.sub_process:
        exec_ctx = action.sub_process.execution_context
        vote_processes = exec_ctx.get_involved_collection(
            'vote_processes')
        opened_vote_processes = [process for process in vote_processes
                                 if not process._finished]
        if opened_vote_processes:
            close_votes(context, request, opened_vote_processes)


def start_ballot_proc(context, process_id):
    def_container = dace_find_service('process_definition_container')
    runtime = dace_find_service('runtime')
    proc = None
    if process_id:
        pd = def_container.get_definition(process_id)
        proc = pd()
        proc.__name__ = proc.id
        runtime.addtoproperty('processes', proc)
        proc.defineGraph(pd)
        proc.execution_context.add_involved_entity(
            'content', context)
        proc.execute()

    return proc


def ballot_result(vote_action, default_value=False):
    ballots = getattr(vote_action.sub_process, 'ballots', [])
    if ballots:
        report = ballots[0].report
        report.calculate_votes()
        if not report.voters:
            return default_value

        electeds = report.get_electeds()
        if electeds is None:
            return False
        else:
            return True

    return default_value


def start_ballot(
    context, author, request,
    root, electors, process_id,
    role='LocalModerator',
    before_start=None):
    if role:
        for elector in electors:
            grant_roles(
                user=elector,
                roles=((role, context),))

    # start a moderation process
    ballot_proc = start_ballot_proc(
        context, process_id)
    if ballot_proc:
        ballot_proc.execution_context.add_involved_collection(
            'electors', electors)
        context.addtoproperty('ballot_processes', ballot_proc)
        if before_start:
            before_start(ballot_proc)

        ballot_proc.execute_action(
            context, request, 'start_ballot', {})

    return ballot_proc


def remove_vote_processes(ballot_action, runtime):
    ballot_process = ballot_action.sub_process
    if ballot_process:
        runtime.delfromproperty('processes', ballot_process)
        exec_ctx = ballot_process.execution_context
        vote_processes = exec_ctx.get_involved_collection(
            'vote_processes')
        for v_proc in vote_processes:
            runtime.delfromproperty('processes', v_proc)


def remove_ballot_processes(content, runtime, exclude=[]):
    processes = content.ballot_processes
    if exclude:
        processes = [p for p in processes if p.id not in exclude]

    for ballot_proc in processes:
        a_vote_actions = ballot_proc.get_actions('start_ballot')
        if a_vote_actions:
            remove_vote_processes(a_vote_actions[0], runtime)

        runtime.delfromproperty('processes', ballot_proc)


def remove_elector_vote_processes(ballot_action, user):
    ballot_process = ballot_action.sub_process
    ballots = ballot_process.ballots
    for ballot in ballots:
        report = ballot.report
        if user in report.electors and user not in report.voters:
            report.delfromproperty('electors', user)


def remove_elector_from_ballot_processes(content, user, exclude=[]):
    processes = content.ballot_processes
    if exclude:
        processes = [p for p in processes if p.id not in exclude]

    for ballot_proc in processes:
        a_vote_actions = ballot_proc.get_actions('start_ballot')
        if a_vote_actions:
            remove_elector_vote_processes(a_vote_actions[0], user)


def get_ballot_alert_data(
    context, request,
    root, electors):
    alert_data = get_entity_data(context, 'subject', request)
    moderators_str = ""
    for index, elector in enumerate(electors):
        elector_data = get_user_data(
            elector, 'subject', request)
        elector_data['subject_email'] = elector.email
        elector_data['index'] = str(index+1)
        moderator_str = MODERATOR_DATA.format(
            **elector_data)
        moderators_str += "\n" + moderator_str

    alert_data['moderators'] = moderators_str
    alert_data['url_terms_of_use'] = request.resource_url(
        root.terms_of_use, '@@index')
    alert_data['url_moderation_rules'] = request.resource_url(
        root.moderation_rules, '@@index')
    duration = getattr(root, 'duration_moderation_vote', 7)
    date_end = datetime.datetime.now() + \
        datetime.timedelta(days=duration)
    alert_data['date_end_vote'] = to_localized_time(
        date_end, request, translate=True)
    alert_data['duration'] = getattr(root, 'duration_moderation_vote', 7)
    alert_data['novaideo_title'] = root.title
    return alert_data
