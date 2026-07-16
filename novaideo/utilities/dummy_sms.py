# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""A sink SMS service for the controlled wake-up of a migrated
instance (see docs/production-migration): logs, sends nothing.
"""
import logging

log = logging.getLogger('novaideo.sms')


class DummySMSService(object):
    """pyramid_sms service that records instead of sending."""

    def __init__(self, request):
        self.request = request

    def send_sms(self, number, text_body, sender=None):
        """Log the send at aggregate level (never the body)."""
        log.info('DummySMSService: 1 SMS withheld (wake-up profile)')

    # historical alias used by some call sites
    send = send_sms
