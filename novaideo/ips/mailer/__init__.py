# Copyright (c) 2014-2022 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi, Michaël Launay

import transaction
from transaction._transaction import Status

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Attachment, Message
from pyramid.threadlocal import get_current_request

import sys

def mailer_send(subject="!",
                sender=None,
                recipients=[],
                body=None,
                html=None,
                attachments=[]):
    try:
        request = get_current_request()
        postmaster = request.registry.settings['mail.default_sender']
        #Due to spf restrictions we can't use sender email for the "From" field
        # but only for the "Reply-To" one.
        extra_headers = {"Reply-To":sender} if sender else None

        mailer = get_mailer(request)
        message = Message(subject=subject,
                          sender=postmaster,
                          recipients=recipients,
                          body=body,
                          extra_headers = extra_headers,
                          html=html)
        for attachment in attachments:
            attachment = Attachment(attachment.title,
                                    attachment.mimetype,
                                    attachment)
            message.attach(attachment)

        if transaction.get().status == Status.COMMITTED:
            mailer.send_immediately(message)
        else:
            mailer.send(message)

    except Exception as exception:
        print(f"Error {exception}", file=sys.stderr)
