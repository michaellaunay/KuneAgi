# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""The Registration arc (anonymous self-registration).

Behaviour-level characterisation of ``registrationmanagement`` — and
one MODERNISATION REGRESSION fixed along the way: substanced's
password API drifted (the era class exposed ``pwd_manager``, the
modern one a ``hash_new_password`` staticmethod), which crashed the
``Preregistration`` constructor on Python 3.12; ``person.py`` now
honours whichever is present, proven end to end by
``check_password`` after confirmation. Pinned contracts:

- the ``registration`` action answers to the ANONYMOUS visitor on the
  root and the ``only_invitation`` setting closes it; the SiteAdmin
  sees it too — the dace-level override that shows every action to
  the site administrator;
- the constructor ENCODES the password immediately
  (``initial_password`` is a bcrypt hash, never the clear text);
- registering stamps the preregistration (state ``['pending']``,
  random-token ``__name__``, deadline = creation + 4 days) and
  answers the submitted redirect;
- the gates: the anonymous visitor holds ``confirmregistration``
  ALONE; the admin holds the quintet with ``remind``/``remove``;
- confirming creates the Person (users key normalised by
  ``name_chooser`` — ``'Bob-B'``), active, ``Member`` + ``Owner``,
  the password verifying across the whole chain, removes the
  preregistration and answers the auto-login redirect;
- an EXPIRED preregistration loses every anonymous action
  (``is_expired`` closes the processsecurity gate);
- the admin's ``remove`` deletes a pending preregistration outright.
"""
import datetime

import pytz
from pyramid.httpexceptions import HTTPFound

from dace.util import getAllBusinessAction
from dace.objectofcollaboration.principal.util import get_roles

from novaideo.testing import FunctionalTests
from novaideo.content.person import Preregistration


class TestRegistrationArc(FunctionalTests):

    def setUp(self):
        super(TestRegistrationArc, self).setUp()
        self.default_novaideo_config()
        self.root = self.request.root
        self.admin = self.request.user
        # substanced's audit subscriber (LoggedIn) reads request.context
        self.request.context = self.root

    def _run(self, context, node_id, appstruct):
        for action in getAllBusinessAction(context, self.request):
            if action.node_id == node_id:
                return action.execute(context, self.request, appstruct)
        raise AssertionError('action not available: ' + node_id)

    def _uids(self, context):
        return set(action.process_id + '.' + action.node_id
                   for action in getAllBusinessAction(
                       context, self.request))

    def _register(self, first_name='Bob', last_name='B',
                  email='bob@example.com', password='bobpass'):
        self.request.user = None
        preregistration = Preregistration(
            first_name=first_name, last_name=last_name,
            email=email, password=password)
        response = self._run(self.root, 'registration',
                             {'_object_data': preregistration})
        return self.root.preregistrations[-1], response

    def test_registration_is_anonymous_and_gated_by_only_invitation(self):
        self.request.user = None
        self.assertIn('registrationmanagement.registration',
                      self._uids(self.root))
        self.root.only_invitation = True
        self.assertNotIn('registrationmanagement.registration',
                         self._uids(self.root))
        self.root.only_invitation = False
        self.request.user = self.admin
        # dace-level rule: SiteAdmin overrides the role gates and
        # sees every action — registration included
        self.assertIn('registrationmanagement.registration',
                      self._uids(self.root))

    def test_constructor_encodes_the_password(self):
        preregistration = Preregistration(
            first_name='Bob', last_name='B',
            email='bob@example.com', password='bobpass')
        hashed = preregistration.initial_password
        self.assertTrue(hashed)
        self.assertNotEqual(hashed, 'bobpass')
        if isinstance(hashed, bytes):
            hashed = hashed.decode('utf-8')
        self.assertTrue(hashed.startswith('$2'))

    def test_registration_stamps_the_preregistration(self):
        preregistration, response = self._register()
        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(len(self.root.preregistrations), 1)
        self.assertEqual(preregistration.state, ['pending'])
        self.assertTrue(10 <= len(preregistration.__name__) <= 15)
        self.assertIs(preregistration.is_expired, False)
        deadline = (preregistration.get_deadline_date()
                    - preregistration.created_at)
        self.assertEqual(deadline.days, 4)

    def test_gates_on_a_pending_preregistration(self):
        preregistration, _ = self._register()
        # the anonymous visitor holds the confirmation alone
        self.assertEqual(self._uids(preregistration),
                         {'registrationmanagement.confirmregistration'})
        self.request.user = self.admin
        self.assertEqual(self._uids(preregistration), {
            'novaideoviewmanager.seehistory',
            'registrationmanagement.confirmregistration',
            'registrationmanagement.remind',
            'registrationmanagement.remove',
            'registrationmanagement.see_registration'})

    def test_confirm_creates_the_person_and_logs_in(self):
        preregistration, _ = self._register()
        users = self.root['principals']['users']
        users_before = len(users)
        response = self._run(preregistration, 'confirmregistration', {})
        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(len(users), users_before + 1)
        # name_chooser normalises the users key
        person = users['Bob-B']
        self.assertEqual(person.state, ['active'])
        self.assertEqual(sorted(get_roles(person)), ['Member', 'Owner'])
        # the whole encode -> store -> verify chain holds
        self.assertTrue(person.check_password('bobpass'))
        self.assertEqual(len(self.root.preregistrations), 0)

    def test_expired_preregistration_closes_every_anonymous_gate(self):
        preregistration, _ = self._register()
        preregistration.deadline_date = (
            datetime.datetime.now(tz=pytz.UTC)
            - datetime.timedelta(days=1))
        self.assertIs(preregistration.is_expired, True)
        self.assertEqual(self._uids(preregistration), set())

    def test_admin_remove_deletes_outright(self):
        preregistration, _ = self._register()
        self.request.user = self.admin
        self._run(preregistration, 'remove', {})
        self.assertEqual(len(self.root.preregistrations), 0)
