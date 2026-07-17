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
from novaideo.content.comment import Comment
from novaideo.content.question import Question
from novaideo.tests.example.app import add_user


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

    def _action_payload(self, uid, values=None, context=None):
        context = context if context is not None else self.idea
        for action in getAllBusinessAction(context, self.request):
            if action.process_id + '.' + action.node_id == uid:
                return action, pseudo_react.get_all_updated_data(
                    action, self.request, context, DummyView(values))
        raise AssertionError('action not available: ' + uid)

    def _payload(self, uid, values=None, context=None):
        return self._action_payload(uid, values, context)[1]

    def _uids(self, context):
        return sorted(set(
            a.process_id + '.' + a.node_id
            for a in getAllBusinessAction(context, self.request)
            if (a.process_id + '.' + a.node_id)
            in pseudo_react.METADATA_GETTERS))

    def _publish_idea(self):
        self._action('ideamanagement.publish').execute(
            self.idea, self.request, {})

    def _add_alice(self):
        return add_user({'first_name': 'Alice', 'last_name': 'A',
                         'email': 'alice@example.com',
                         'password': 'alice'}, self.request)

    def _assert_redirect_family(self, result, uid=''):
        self.assertEqual(
            sorted(result),
            ['action', 'alert_msg', 'alert_type', 'is_excuted',
             'new_body', 'object_views_to_update', 'redirect_url',
             'resources', 'view', 'view_name'], uid)
        self.assertEqual(result['action'], 'redirect_action')
        self.assertEqual(result['alert_type'], 'success')
        self.assertIs(result['is_excuted'], False)

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


    def test_action_sets_by_role(self):
        """The available getter set is role-dependent, exactly."""
        self._publish_idea()
        admin_set = set(self._uids(self.idea))
        self.assertEqual(admin_set, {
            'eventmanagement.create', 'ideamanagement.comment',
            'ideamanagement.duplicate', 'ideamanagement.present',
            'novaideoabstractprocess.select', 'reportsmanagement.report'})
        admin = self.request.user
        alice = self._add_alice()
        self.request.user = alice
        alice_set = set(self._uids(self.idea))
        # a plain member additionally gets the token actions
        self.assertEqual(alice_set - admin_set,
                         {'ideamanagement.support', 'ideamanagement.oppose'})
        # the comment's author gets edit/remove; another user does not
        comment = Comment(comment='The comment', intention='Remark')
        self._payload('ideamanagement.comment')  # composer only reads
        for action in getAllBusinessAction(self.idea, self.request):
            if action.node_id == 'comment':
                action.execute(self.idea, self.request,
                               {'_object_data': comment})
                break
        comment = self.idea.channel.comments[-1]
        alice_on_comment = set(self._uids(comment))
        self.request.user = admin
        admin_on_comment = set(self._uids(comment))
        self.assertEqual(
            alice_on_comment - admin_on_comment,
            {'commentmanagement.edit', 'commentmanagement.remove'})

    def test_payload_footer_comment_and_present(self):
        self._publish_idea()
        for uid, title, icon in (
                ('ideamanagement.comment', 'Comment', 'ion-chatbubble'),
                ('ideamanagement.present', 'Share',
                 'glyphicon glyphicon-share-alt')):
            action, result = self._action_payload(uid)
            # the component id is built on the ACTION's own oid
            component = '%s-%s' % (get_oid(action), get_oid(self.idea))
            self.assertEqual(
                sorted(result),
                ['action', 'action_icon', 'action_item_nb', 'action_title',
                 'components', 'new_body', 'object_views_to_update',
                 'resources', 'view'], uid)
            self.assertEqual(result['action'], 'footer_action')
            self.assertEqual(result['action_title'], title)
            self.assertEqual(result['action_icon'], icon)
            self.assertEqual(result['action_item_nb'], 0)
            self.assertEqual(result['components'], [component])
            self.assertIsNone(result['new_body'])

    def test_payload_support_and_oppose(self):
        self._publish_idea()
        self.request.user = self._add_alice()
        for uid, message in (
                ('ideamanagement.support',
                 'Now you support the content Idea title.'),
                ('ideamanagement.oppose',
                 'You are now opposed to the content Idea title.')):
            result = self._payload(uid)
            self.assertEqual(
                sorted(result),
                ['action', 'alert_msg', 'alert_type', 'components',
                 'counters-to-update', 'object_views_to_update',
                 'objects_to_hide', 'resources', 'view'], uid)
            self.assertEqual(result['action'], 'support_action')
            self.assertEqual(result['alert_msg'], message)
            self.assertEqual(result['alert_type'], 'success')
            self.assertEqual(result['components'],
                             [str(get_oid(self.idea))])
            self.assertEqual(result['objects_to_hide'], [])
            self.assertEqual(result['counters-to-update'],
                             ['component-navbar-mysupports'])

    def test_payload_select(self):
        self._publish_idea()
        result = self._payload('novaideoabstractprocess.select')
        self.assertEqual(
            sorted(result),
            ['action', 'counters-to-update', 'object_views_to_update',
             'resources', 'view'])
        self.assertEqual(result['action'], 'footer_action')
        self.assertEqual(result['counters-to-update'],
                         ['component-navbar-myselections'])

    def test_payload_comment_family(self):
        self._publish_idea()
        self.request.user = self._add_alice()
        comment = Comment(comment='The comment', intention='Remark')
        for action in getAllBusinessAction(self.idea, self.request):
            if action.node_id == 'comment':
                action.execute(self.idea, self.request,
                               {'_object_data': comment})
                break
        comment = self.idea.channel.comments[-1]
        result = self._payload('commentmanagement.edit', context=comment)
        self.assertEqual(sorted(result),
                         ['action', 'object_views_to_update', 'resources',
                          'status', 'view'])
        self.assertEqual(result['action'], 'footer_action')
        self.assertIs(result['status'], False)
        result = self._payload('commentmanagement.remove', context=comment)
        self.assertEqual(sorted(result),
                         ['action', 'object_views_to_update', 'resources',
                          'view'])
        self.assertEqual(result['action'], 'footer_action')
        result = self._payload('commentmanagement.pin', context=comment)
        self._assert_redirect_family(result, 'pin')
        result = self._payload('commentmanagement.respond', context=comment)
        self.assertEqual(result['action'], 'footer_action')
        self.assertEqual(result['action_title'], 'Comment')
        self.assertEqual(result['action_item_nb'], 1)

    def test_question_flow(self):
        question = Question(title='Question title', text='Question text',
                            keywords=['k1'])
        root = self.request.root
        getAllBusinessAction(
            root, self.request, process_id='questionmanagement',
            node_id='creat')[0].execute(
            root, self.request, {'_object_data': question})
        question = root.questions[-1]
        self.assertEqual(set(self._uids(question)), {
            'novaideoabstractprocess.select', 'questionmanagement.answer',
            'questionmanagement.archive', 'questionmanagement.comment',
            'questionmanagement.edit', 'questionmanagement.oppose',
            'questionmanagement.present', 'questionmanagement.support',
            'reportsmanagement.report'})
        self._assert_redirect_family(
            self._payload('questionmanagement.answer', context=question),
            'answer')
        self._assert_redirect_family(
            self._payload('questionmanagement.archive', context=question),
            'archive')
