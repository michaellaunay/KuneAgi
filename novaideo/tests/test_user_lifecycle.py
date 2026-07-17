# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Person lifecycle in ``user_management`` (T4b).

Behaviour-level characterisation of the security core. Pinned:

- a fresh member is ``['active']`` with the roles
  ``['Member', 'Owner']``;
- the gates are exact: the admin extras on a person are
  ``{select, user_edit_organization, assign_roles, deactivate,
  discuss}`` (one cannot ``discuss`` with oneself);
- ``deactivate`` collapses the admin gates to
  ``{seehistory, activate, see, see_notations}``; ``activate``
  restores ``['active']``;
- ``assign_roles`` REQUIRES ``roles`` and REPLACES the assignable
  set — ``Member`` disappears, the ``Owner`` relation is preserved;
- ``Edit.start`` requires the NESTED ``change_password`` mapping
  (``{changepassword, currentuserpassword, password}``): the
  no-change mode keeps the password and still bumps ``modified_at``;
  the change mode (correct current password) switches it;
- ``get_api_token`` requires the ``password`` and installs a
  32-character ``api_token`` behind an ``HTTPFound``;
- ``quit`` is a REQUEST, not the act: it redirects and leaves the
  state ``['active']`` (the confirmation arrives by mail through
  ``ConfirmQuitRequest``).
"""
from pyramid.httpexceptions import HTTPFound

from dace.util import getAllBusinessAction
from dace.objectofcollaboration.principal.util import get_roles, has_role

from novaideo.testing import FunctionalTests
from novaideo.tests.example.app import add_user


class TestPersonLifecycle(FunctionalTests):

    def setUp(self):
        super(TestPersonLifecycle, self).setUp()
        self.default_novaideo_config()
        self.admin = self.request.user
        self.alice = add_user(
            {'first_name': 'Alice', 'last_name': 'A',
             'email': 'alice@example.com', 'password': 'alice'},
            self.request)

    def _run(self, context, node_id, appstruct):
        for action in getAllBusinessAction(context, self.request):
            if action.node_id == node_id:
                return action.execute(context, self.request, appstruct)
        raise AssertionError('action not available: ' + node_id)

    def _uids(self, context):
        return set(action.process_id + '.' + action.node_id
                   for action in getAllBusinessAction(
                       context, self.request))

    def test_person_shape(self):
        self.assertEqual(self.alice.state, ['active'])
        self.assertEqual(sorted(get_roles(self.alice)),
                         ['Member', 'Owner'])
        self.assertEqual(self.alice.title, 'Alice A')

    def test_role_gates_exact(self):
        admin_set = self._uids(self.alice)
        self.assertEqual(admin_set, {
            'novaideoabstractprocess.select',
            'organizationmanagement.user_edit_organization',
            'usermanagement.assign_roles', 'usermanagement.deactivate',
            'usermanagement.discuss', 'usermanagement.edit',
            'usermanagement.extract_alerts',
            'usermanagement.get_api_token', 'usermanagement.quit',
            'usermanagement.see', 'usermanagement.see_notations'})
        self.request.user = self.alice
        # one cannot discuss with oneself; the rest are admin extras
        self.assertEqual(
            admin_set - self._uids(self.alice),
            {'novaideoabstractprocess.select',
             'organizationmanagement.user_edit_organization',
             'usermanagement.assign_roles', 'usermanagement.deactivate',
             'usermanagement.discuss'})

    def test_deactivate_collapses_the_gates(self):
        self._run(self.alice, 'deactivate', {})
        self.assertEqual(self.alice.state, ['deactivated'])
        self.assertEqual(self._uids(self.alice), {
            'novaideoviewmanager.seehistory', 'usermanagement.activate',
            'usermanagement.see', 'usermanagement.see_notations'})

    def test_activate_restores(self):
        self._run(self.alice, 'deactivate', {})
        self._run(self.alice, 'activate', {})
        self.assertEqual(self.alice.state, ['active'])

    def test_assign_roles_requires_and_replaces(self):
        self.assertRaises(KeyError, self._run,
                          self.alice, 'assign_roles', {})
        self._run(self.alice, 'assign_roles', {'roles': ['Moderator']})
        # assignment REPLACES: Member is gone, the Owner relation stays
        self.assertEqual(sorted(get_roles(self.alice)),
                         ['Moderator', 'Owner'])
        self.assertTrue(has_role(('Moderator',), self.alice))

    def test_edit_requires_the_nested_mapping(self):
        self.request.user = self.alice
        self.assertRaises(KeyError, self._run,
                          self.alice, 'edit', {'first_name': 'Alicia'})

    def test_edit_password_modes(self):
        self.request.user = self.alice
        before = self.alice.modified_at
        self._run(self.alice, 'edit',
                  {'change_password': {'changepassword': False,
                                       'currentuserpassword': '',
                                       'password': ''}})
        self.assertTrue(self.alice.check_password('alice'))
        self.assertNotEqual(self.alice.modified_at, before)
        self._run(self.alice, 'edit',
                  {'change_password': {'changepassword': True,
                                       'currentuserpassword': 'alice',
                                       'password': 'newpass'}})
        self.assertTrue(self.alice.check_password('newpass'))
        self.assertFalse(self.alice.check_password('alice'))

    def test_get_api_token(self):
        self.request.user = self.alice
        self.assertRaises(KeyError, self._run,
                          self.alice, 'get_api_token', {})
        response = self._run(self.alice, 'get_api_token',
                             {'password': 'alice'})
        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(len(self.alice.api_token), 32)

    def test_quit_is_a_request_not_the_act(self):
        self.request.user = self.alice
        response = self._run(self.alice, 'quit', {})
        self.assertIsInstance(response, HTTPFound)
        # the account stays active until the mailed confirmation
        self.assertEqual(self.alice.state, ['active'])
