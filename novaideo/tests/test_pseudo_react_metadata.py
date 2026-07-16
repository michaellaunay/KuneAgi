# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Functional tests of the ``pseudo_react`` metadata composers (T2a).

One real application (the M4 harness), many payload asserts: the
composers answer the SPA bridge after an action executes — these tests
pin the payload contract per action family, plus the two dispatch
registries. Conventions pinned:

- in the composers' signature, ``api`` is the calling *view*: only its
  ``params(name)`` is consumed (a dict-backed dummy suffices);
- the counters of ``COUNTERS_COMPONENTS`` share the same signature;
- ``'action': 'redirect_action'`` is the common payload marker, and
  the historical ``is_excuted`` spelling is part of the contract.

Runs on both stacks (the golden-master container executes it too).
"""
import re

from substanced.util import get_oid

from dace.util import getAllBusinessAction

import novaideo.views  # primes the pseudo_react <-> views import cycle
from novaideo.utilities import pseudo_react
from novaideo.testing import FunctionalTests
from novaideo.content.idea import Idea


class DummyView(object):
    """The composers only consume ``api.params(name)``."""

    def __init__(self, values=None):
        self.values = values or {}

    def params(self, name):
        return self.values.get(name)


class TestPseudoReactMetadata(FunctionalTests):

    def setUp(self):
        super(TestPseudoReactMetadata, self).setUp()
        self.default_novaideo_config()
        context = self.request.root
        idea = Idea(title="Idea title", text="Idea text",
                    keywords=["keyword 1", "keyword 2"])
        action = getAllBusinessAction(
            context, self.request,
            process_id='ideamanagement', node_id='creat')[0]
        action.execute(context, self.request, {'_object_data': idea})
        self.idea = context.ideas[-1]

    def _action(self, uid):
        for action in getAllBusinessAction(self.idea, self.request):
            if action.process_id + '.' + action.node_id == uid:
                return action
        raise AssertionError('action not available: ' + uid)

    def _payload(self, uid, values=None):
        return pseudo_react.get_all_updated_data(
            self._action(uid), self.request, self.idea, DummyView(values))

    def test_metadata_registry_shape(self):
        registry = pseudo_react.METADATA_GETTERS
        self.assertEqual(len(registry), 121)
        for uid, getter in registry.items():
            self.assertTrue(re.match(r'^[a-z_]+\.[a-z_]+$', uid), uid)
            self.assertTrue(callable(getter), uid)

    def test_counters_registry_shape(self):
        registry = pseudo_react.COUNTERS_COMPONENTS
        self.assertEqual(len(registry), 16)
        for component_id, counter in registry.items():
            self.assertTrue(callable(counter), component_id)

    def test_without_action(self):
        view = DummyView()
        self.assertEqual(
            pseudo_react.get_all_updated_data(
                None, self.request, self.idea, view),
            {'action': None, 'view': view})

    def test_payload_abandon(self):
        result = self._payload('ideamanagement.abandon')
        self.assertEqual(
            sorted(result),
            ['action', 'alert_msg', 'alert_type', 'object_views_to_update',
             'objects_to_hide', 'redirect_url', 'resources', 'view',
             'view_name'])
        self.assertEqual(result['action'], 'redirect_action')
        self.assertIsNone(result['redirect_url'])
        self.assertEqual(result['alert_msg'], 'The idea has been archived.')
        self.assertEqual(result['alert_type'], 'success')
        oid = str(get_oid(self.idea))
        self.assertEqual(result['objects_to_hide'],
                         ['listing_' + oid, 'listingbloc_' + oid])

    def test_payload_duplicate(self):
        result = self._payload('ideamanagement.duplicate')
        self.assertEqual(
            sorted(result),
            ['action', 'new_body', 'object_views_to_update',
             'redirect_url', 'resources', 'view'])
        self.assertEqual(result['action'], 'redirect_action')
        self.assertIsNone(result['redirect_url'])
        self.assertIsNone(result['new_body'])

    def test_payload_edit_and_publish(self):
        for uid in ('ideamanagement.edit', 'ideamanagement.publish'):
            result = self._payload(uid)
            self.assertEqual(
                sorted(result),
                ['action', 'alert_msg', 'alert_type', 'is_excuted',
                 'new_body', 'object_views_to_update', 'redirect_url',
                 'resources', 'view', 'view_name'], uid)
            self.assertEqual(result['action'], 'redirect_action')
            self.assertIsNone(result['redirect_url'])
            self.assertIsNone(result['alert_msg'])
            self.assertEqual(result['alert_type'], 'success')
            self.assertIs(result['is_excuted'], False)
            self.assertIsNone(result['view_name'])
            self.assertIsNone(result['new_body'])

    def test_counters_payloads(self):
        from dace.objectofcollaboration.principal.util import get_current
        user = get_current(self.request)
        counters = pseudo_react.COUNTERS_COMPONENTS
        view = DummyView()
        home_ideas = counters['home-ideas-counter'](
            None, self.request, self.idea, view, user=user)
        self.assertEqual(home_ideas,
                         {'home-ideas-counter.title': 'Ideas (0)'})
        mycontents = counters['component-navbar-mycontents'](
            None, self.request, self.idea, view, user=user)
        self.assertEqual(
            mycontents.get('component-navbar-mycontents.item_nb'), 0)
        proposals = counters['home-proposals-counter'](
            None, self.request, self.idea, view, user=user)
        self.assertEqual(proposals, {})
