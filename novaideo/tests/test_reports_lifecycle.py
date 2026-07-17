# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""The report/moderation cycle (``reports_management``).

Behaviour-level characterisation of the social-safety machinery.
Pinned contracts:

- ``report`` is MEMBER-gated (no anonymous) and state-gated on
  ``published`` content;
- reporting appends ``'reported'`` to the content state, files the
  report (``['pending']``, reporter as author) and STARTS the
  ``contentreportdecision`` ballot (the moderator draw excludes the
  content author); reporting stays available while no finished valid
  ballot exists;
- ``censor()`` REPLACES the whole content state with ``['censored']``
  (the per-type ``ISignalableObject`` adapter) and processes the
  pending reports;
- ``restor`` is MODERATOR-gated from ``censored`` and restores the
  original publication states;
- ``ignore()`` removes ``'reported'`` and processes the reports,
  leaving the publication untouched.

The content author is a real Person (``user_locale``) — the raw
substanced admin cannot author reportable content.
"""
from dace.util import getAllBusinessAction

import novaideo.views  # primes the historical import cycle
from novaideo.testing import FunctionalTests
from novaideo.content.idea import Idea
from novaideo.content.report import Report
from novaideo.tests.example.app import add_user
from novaideo.content.processes.reports_management import (
    behaviors as report_behaviors)


class TestReportsLifecycle(FunctionalTests):

    def setUp(self):
        super(TestReportsLifecycle, self).setUp()
        self.default_novaideo_config()
        self.root = self.request.root
        self.admin = self.request.user
        self.request.context = self.root
        self.bob = add_user({'first_name': 'Bob', 'last_name': 'B',
                             'email': 'bob@example.com',
                             'password': 'bob'}, self.request)
        self.alice = add_user({'first_name': 'Alice', 'last_name': 'A',
                               'email': 'alice@example.com',
                               'password': 'alice'}, self.request)
        # the author must be a real Person (user_locale)
        self.request.user = self.bob
        idea = Idea(title='Idea title', text='The text',
                    keywords=['keyword'])
        self._run(self.root, 'creat', {'_object_data': idea},
                  'ideamanagement')
        self.idea = self.root.ideas[-1]
        self._run(self.idea, 'publish', {})
        self.request.user = self.alice

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

    def _report(self):
        report = Report(reporting_reasons=['other'],
                        details='The details')
        self._run(self.idea, 'report', {'_object_data': report})
        return self.idea.reports[-1]

    def test_report_is_member_gated_and_state_gated(self):
        self.assertIn('reportsmanagement.report', self._uids(self.idea))
        self.request.user = None
        self.assertNotIn('reportsmanagement.report',
                         self._uids(self.idea))
        # state gate: an unpublished idea is not reportable
        self.request.user = self.bob
        draft = Idea(title='Draft', text='The text',
                     keywords=['keyword'])
        self._run(self.root, 'creat', {'_object_data': draft},
                  'ideamanagement')
        draft = self.root.ideas[-1]
        self.request.user = self.alice
        self.assertNotIn('reportsmanagement.report', self._uids(draft))

    def test_report_marks_and_starts_the_ballot(self):
        report = self._report()
        self.assertIn('reported', self.idea.state)
        self.assertEqual(report.state, ['pending'])
        self.assertIs(report.author, self.alice)
        self.assertEqual(
            [b.id for b in self.idea.ballot_processes],
            ['contentreportdecision'])
        # no finished valid ballot yet: reporting stays available
        self.assertIn('reportsmanagement.report', self._uids(self.idea))

    def test_censor_replaces_the_whole_state(self):
        report = self._report()
        report_behaviors.censor(self.idea, self.request, self.root)
        self.assertEqual(self.idea.state, ['censored'])
        self.assertEqual(report.state, ['processed'])

    def test_restor_is_moderator_gated(self):
        self._report()
        report_behaviors.censor(self.idea, self.request, self.root)
        self.assertNotIn('reportsmanagement.restor', self._uids(self.idea))
        self.request.user = self.admin
        self._run(self.alice, 'assign_roles', {'roles': ['Moderator']})
        self.request.user = self.alice
        self.assertIn('reportsmanagement.restor', self._uids(self.idea))
        self._run(self.idea, 'restor', {})
        # the original publication states come back
        self.assertEqual(self.idea.state,
                         ['submitted_support', 'published'])

    def test_ignore_processes_and_unmarks(self):
        report = self._report()
        report_behaviors.ignore(self.idea, self.request, self.root)
        self.assertNotIn('reported', self.idea.state)
        self.assertIn('published', self.idea.state)
        self.assertEqual(report.state, ['processed'])

    def test_report_content_shape(self):
        report = self._report()
        self.assertEqual(report.reporting_reasons, ['other'])
        reasons = report.get_reporting_reasons()
        self.assertEqual(len(reasons), 1)
        self.assertEqual(len(reasons[0]), 2)
        # the reason referential is closed: unknown keys KeyError
        report.reporting_reasons = ['unknown_reason']
        self.assertRaises(KeyError, report.get_reporting_reasons)
