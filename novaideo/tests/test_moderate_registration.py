# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""The ``moderate_registration`` variant: the registration ballot.

The candidacy is judged before the door opens. Pinned contracts:

- under moderation, registering does NOT send the confirmation: the
  preregistration stays ``['pending']``, a ``registrationmoderation``
  ballot is attached (the elector draw is a random pick among ALL
  members — no author to exclude), the electors are granted
  ``('LocalModerator', preregistration)`` and vote ON the
  preregistration; the anonymous ``confirmregistration`` gate is
  CLOSED while pending;
- acceptance REPLACES the state with ``['accepted']``, opens the
  gate, and the whole entry path completes through moderation
  (confirmation creates the Person);
- refusal REMOVES the candidacy from the root outright;
- SILENT electors refuse: ``ballot_result(self)`` defaults to False
  here — the asymmetry of mercy with the report decision, whose
  silence defaults to ignore;
- the no-electors fallback accepts outright and the entry path
  completes (FIXED 2026-07-17, was latent bug #4: the under-review
  notification — ballot-bound ``alert_data`` — moved into the ballot
  branch, ending the ``UnboundLocalError`` torn write of the imported
  historical source).

The decision node completes at the ballot deadline in production; the
tests invoke its ``after_execution`` after the last vote — the very
code path the deadline runs.
"""
from dace.util import getAllBusinessAction
from dace.objectofcollaboration.principal.util import has_role

from novaideo.tests.example.app import add_user
import novaideo.views  # primes the historical import cycle
from novaideo.testing import FunctionalTests
from novaideo.content.person import Preregistration


class TestModerateRegistration(FunctionalTests):

    def setUp(self):
        super(TestModerateRegistration, self).setUp()
        self.default_novaideo_config()
        self.root = self.request.root
        self.request.context = self.root
        self.root.moderate_registration = True

    def _members(self):
        return [add_user({'first_name': name, 'last_name': name[0],
                          'email': '%s@example.com' % name.lower(),
                          'password': 'x'}, self.request)
                for name in ('Carol', 'Dave', 'Eve')]

    def _run(self, context, node_id, appstruct, process_id=None):
        for action in getAllBusinessAction(context, self.request):
            if action.node_id == node_id and (
                    process_id is None or action.process_id == process_id):
                return action.execute(context, self.request, appstruct)
        raise AssertionError('action not available: ' + node_id)

    def _uids(self, context):
        return set(action.process_id + '.' + action.node_id
                   for action in getAllBusinessAction(
                       context, self.request))

    def _register(self, first_name='Bob', last_name='B',
                  email='bob@example.com'):
        self.request.user = None
        preregistration = Preregistration(
            first_name=first_name, last_name=last_name,
            email=email, password='pass')
        self._run(self.root, 'registration',
                  {'_object_data': preregistration})
        return self.root.preregistrations[-1]

    def _decision_action(self, preregistration):
        return preregistration.ballot_processes[0].get_actions(
            'start_ballot')[0]

    def _electors(self, preregistration):
        action = self._decision_action(preregistration)
        return list(action.sub_process.ballots[0].report.electors)

    def _vote_all(self, preregistration, value):
        for elector in self._electors(preregistration):
            self.request.user = elector
            self._run(preregistration, 'vote', {'vote': value})

    def _decide(self, preregistration):
        self._decision_action(preregistration).after_execution(
            preregistration, self.request)

    def test_no_electors_fallback_accepts_at_once(self):
        """FIXED (2026-07-17, was latent bug #4): the under-review
        notification moved into the ballot branch — with no member to
        draw, the fallback accepts outright and the whole entry path
        completes."""
        preregistration = self._register()
        self.assertEqual(preregistration.state, ['accepted'])
        # the anonymous confirmation gate is OPEN at once
        self.assertIn('registrationmanagement.confirmregistration',
                      self._uids(preregistration))
        self._run(preregistration, 'confirmregistration', {})
        self.assertIn('Bob-B', self.root['principals']['users'])

    def test_ballot_path_gates_the_confirmation(self):
        self._members()
        preregistration = self._register()
        self.assertEqual(preregistration.state, ['pending'])
        self.assertEqual(preregistration.ballot_processes[0].id,
                         'registrationmoderation')
        electors = self._electors(preregistration)
        self.assertEqual(len(electors), 3)
        for elector in electors:
            self.assertTrue(has_role(
                ('LocalModerator', preregistration), elector))
        # the anonymous confirmation gate is CLOSED while pending
        self.request.user = None
        self.assertNotIn('registrationmanagement.confirmregistration',
                         self._uids(preregistration))

    def test_vote_is_elector_gated(self):
        self._members()
        preregistration = self._register()
        self.request.user = self._electors(preregistration)[0]
        self.assertIn('referendumprocess.vote',
                      self._uids(preregistration))
        self.request.user = None
        self.assertNotIn('referendumprocess.vote',
                         self._uids(preregistration))

    def test_acceptance_opens_the_gate(self):
        self._members()
        preregistration = self._register()
        self._vote_all(preregistration, True)
        self._decide(preregistration)
        self.assertEqual(preregistration.state, ['accepted'])
        self.request.user = None
        self.assertIn('registrationmanagement.confirmregistration',
                      self._uids(preregistration))
        # the whole entry path completes through moderation
        self._run(preregistration, 'confirmregistration', {})
        self.assertIn('Bob-B', self.root['principals']['users'])

    def test_refusal_removes_the_candidacy(self):
        self._members()
        preregistration = self._register()
        self._vote_all(preregistration, False)
        self._decide(preregistration)
        self.assertEqual(len(self.root.preregistrations), 0)
        self.assertIsNone(preregistration.__parent__)

    def test_silent_electors_refuse(self):
        """The asymmetry of mercy: the report decision defaults to
        ignore on silence; the registration decision REFUSES."""
        self._members()
        preregistration = self._register()
        self._decide(preregistration)
        self.assertEqual(len(self.root.preregistrations), 0)
