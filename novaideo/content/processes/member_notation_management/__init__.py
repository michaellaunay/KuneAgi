# Copyright (c) 2016 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

import datetime

from dace.util import getSite

from novaideo import _
from novaideo.content.ballot import Ballot
from novaideo.content.alert import InternalAlertKind
from novaideo.utilities.alerts_utility import (
    alert, get_user_data, get_entity_data)


NOTATIONS = [(-1, '-1'), (0, '0'), (1, '1')]


DEFAULT_NOTATION = '0'


DURATION = datetime.timedelta(days=1000)


def run_notation_process(context, request, user, members):
    if members:
        subjects = [context]
        title = _('Notation of ${member}',
                  mapping={'member': user.title})
        ballot = Ballot('FPTP', members, subjects, DURATION,
                        vote_process_id='membernotationmanagement',
                        group_values=NOTATIONS,
                        group_default=DEFAULT_NOTATION)
        context.addtoproperty('ballots', ballot)
        ballot.title = title
        ballot.report.description_template = 'novaideo:views/templates/ballots/member_notation.pt'
        processes = ballot.run_ballot(context=context)
        for process in processes:
            process.execution_context.add_involved_entity(
                'member', user)
        root = getSite()
        alert_data = get_user_data(user, 'user', request)
        alert_data.update(get_entity_data(user, 'user', request))
        alert(
            'internal', [root], members,
            internal_kind=InternalAlertKind.working_group_alert,
            subjects=[context], alert_kind='member_notation',
            **alert_data)
        alert_data.update(get_entity_data(context, 'subject', request))
        mail_template = root.get_mail_template('member_notation')
        subject = mail_template['subject'].format(
            novaideo_title=root.title,
            **alert_data)
        for member in [a for a in members if getattr(a, 'email', '')]:
            email_data = get_user_data(member, 'recipient', request)
            alert_data.update(email_data)
            message = mail_template['template'].format(
                novaideo_title=root.title,
                **alert_data)
            alert('email', [root.get_site_sender()], [member.email],
                  subject=subject, body=message)
