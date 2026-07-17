# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Invitation lifecycle in ``invitation_management`` (T4c).

Behaviour-level characterisation of the entry path. Pinned:

- ``invite`` takes ``{'invitations': [{'_object_data': Invitation}]}``
  and stamps each one: state ``['pending']``, ``manager`` = the
  inviter, a random-token ``__name__`` (10–15 chars), default roles
  ``['Member']``;
- the gates INVERT across the mail link: the admin holds
  ``{edit, remind, remove, seeinvitation}`` while the ANONYMOUS
  visitor holds ``{accept, refuse, seeinvitation}``;
- ``accept`` requires the ``password``, creates the Person FROM the
  invitation's data (active, granted the invitation roles plus
  ``Owner``, password installed), REMOVES the invitation from the
  root and links it back through ``invitation.person``;
- ``refuse`` is the asymmetric twin: the invitation STAYS at the root,
  marked ``['refused']``, and the anonymous actions collapse to
  ``seeinvitation`` alone (the pending gate closed);
- the admin's ``remove`` deletes a pending invitation outright.
"""
from dace.util import getAllBusinessAction
from dace.objectofcollaboration.principal.util import get_roles

from novaideo.testing import FunctionalTests
from novaideo.content.invitation import Invitation


class TestInvitationLifecycle(FunctionalTests):

    def setUp(self):
        super(TestInvitationLifecycle, self).setUp()
        self.default_novaideo_config()
        self.root = self.request.root
        self.admin = self.request.user

    def _run(self, context, node_id, appstruct):
        for action in getAllBusinessAction(context, self.request):
            if action.node_id == node_id:
                return action.execute(context, self.request, appstruct)
        raise AssertionError('action not available: ' + node_id)

    def _uids(self, context):
        return set(action.process_id + '.' + action.node_id
                   for action in getAllBusinessAction(
                       context, self.request))

    def _invite(self, first_name='Bob', last_name='B',
                email='bob@example.com'):
        invitation = Invitation(first_name=first_name,
                                last_name=last_name, email=email)
        self._run(self.root, 'invite',
                  {'invitations': [{'_object_data': invitation}]})
        return self.root.invitations[-1]

    def test_root_invitation_actions(self):
        root_uids = self._uids(self.root)
        for uid in ('invitationmanagement.add',
                    'invitationmanagement.invite',
                    'invitationmanagement.seeinvitations'):
            self.assertIn(uid, root_uids)

    def test_invite_stamps_the_invitation(self):
        invitation = self._invite()
        self.assertEqual(len(self.root.invitations), 1)
        self.assertEqual(invitation.state, ['pending'])
        self.assertIs(invitation.manager, self.admin)
        self.assertEqual(invitation.roles, ['Member'])
        self.assertTrue(10 <= len(invitation.__name__) <= 15)

    def test_gates_invert_across_the_mail_link(self):
        invitation = self._invite()
        self.assertEqual(self._uids(invitation), {
            'invitationmanagement.edit', 'invitationmanagement.remind',
            'invitationmanagement.remove',
            'invitationmanagement.seeinvitation'})
        self.request.user = None
        self.assertEqual(self._uids(invitation), {
            'invitationmanagement.accept',
            'invitationmanagement.refuse',
            'invitationmanagement.seeinvitation'})

    def test_accept_requires_the_password(self):
        invitation = self._invite()
        self.request.user = None
        self.assertRaises(KeyError, self._run,
                          invitation, 'accept', {'pseudonym': None})

    def test_accept_creates_the_person_and_removes_the_invitation(self):
        invitation = self._invite()
        users = self.root['principals']['users']
        users_before = len(users)
        self.request.user = None
        self._run(invitation, 'accept',
                  {'password': 'bobpass', 'pseudonym': None})
        self.assertEqual(len(users), users_before + 1)
        self.assertEqual(len(self.root.invitations), 0)
        person = invitation.person
        self.assertIsNotNone(person)
        self.assertEqual(person.state, ['active'])
        self.assertEqual(sorted(get_roles(person)), ['Member', 'Owner'])
        self.assertTrue(person.check_password('bobpass'))
        self.assertEqual(person.first_name, 'Bob')

    def test_refuse_marks_in_place(self):
        invitation = self._invite()
        self.request.user = None
        self._run(invitation, 'refuse', {})
        # the asymmetric twin of accept: kept at the root, marked
        self.assertEqual(len(self.root.invitations), 1)
        self.assertEqual(invitation.state, ['refused'])
        # the pending gate closed: only seeing remains
        self.assertEqual(self._uids(invitation),
                         {'invitationmanagement.seeinvitation'})

    def test_admin_remove_deletes_outright(self):
        invitation = self._invite()
        self._run(invitation, 'remove', {})
        self.assertEqual(len(self.root.invitations), 0)
