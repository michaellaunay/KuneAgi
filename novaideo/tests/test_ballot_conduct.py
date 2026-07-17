# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Conducting the ``contentreportdecision`` ballot to its verdict.

The deepening of the report/moderation cycle: the moderators VOTE and
the decision falls. Pinned contracts:

- reporting draws the electors among the members EXCLUDING only the
  content author — the REPORTER is a juror; each elector is granted
  ``('LocalModerator', content)`` and one Referendum ballot is
  attached to the content;
- the ``referendumprocess.vote`` action appears ON THE CONTENT for
  electors only, disappears for whoever has voted, and REQUIRES the
  ``vote`` key (True/False);
- the decision node completes at the BALLOT DEADLINE in production
  (the vote sub-process is timer-closed); the tests invoke the node's
  ``after_execution`` after the last vote — the very code path the
  deadline runs;
- majority AGAINST the content → ``censor``: the state becomes
  ``['censored']``, the reports are processed;
- majority FOR → ``ignore``: the publication is untouched, the
  reports are processed;
- either verdict REVOKES the ``LocalModerator`` grants and CLOSES the
  report action for members (a finished valid ballot blocks
  re-reporting) — the second half of the anti-re-report contract.
"""
from dace.util import getAllBusinessAction
from dace.objectofcollaboration.principal.util import has_role

from novaideo.tests.example.app import add_user
import novaideo.views  # primes the historical import cycle
from novaideo.testing import FunctionalTests
from novaideo.content.idea import Idea
from novaideo.content.report import Report


class TestBallotConduct(FunctionalTests):

    def setUp(self):
        super(TestBallotConduct, self).setUp()
        self.default_novaideo_config()
        self.root = self.request.root
        self.request.context = self.root
        self.bob = self._member('Bob', 'B')
        self.alice = self._member('Alice', 'A')
        self.carol = self._member('Carol', 'C')
        self.dave = self._member('Dave', 'D')
        self.electors = (self.alice, self.carol, self.dave)

    def _member(self, first_name, last_name):
        return add_user(
            {'first_name': first_name, 'last_name': last_name,
             'email': '%s@example.com' % first_name.lower(),
             'password': 'x'}, self.request)

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

    def _reported_idea(self):
        self.request.user = self.bob
        idea = Idea(title='Idea title', text='The text',
                    keywords=['keyword'])
        self._run(self.root, 'creat', {'_object_data': idea},
                  'ideamanagement')
        idea = self.root.ideas[-1]
        self._run(idea, 'publish', {})
        self.request.user = self.alice
        report = Report(reporting_reasons=['other'],
                        details='The details')
        self._run(idea, 'report', {'_object_data': report})
        return idea

    def _decision_action(self, idea):
        return idea.ballot_processes[0].get_actions('start_ballot')[0]

    def _vote(self, idea, who, value):
        self.request.user = who
        self._run(idea, 'vote', {'vote': value})

    def _decide(self, idea):
        # production completes the node at the ballot deadline; the
        # tests run the same code path directly
        self._decision_action(idea).after_execution(idea, self.request)

    def test_ballot_plumbing(self):
        idea = self._reported_idea()
        self.assertEqual(idea.ballot_processes[0].id,
                         'contentreportdecision')
        self.assertEqual(len(idea.ballots), 1)
        report = self._decision_action(idea).sub_process.ballots[0].report
        # the reporter is a juror: only the author is excluded
        self.assertEqual(
            sorted(elector.first_name for elector in report.electors),
            ['Alice', 'Carol', 'Dave'])
        for elector in self.electors:
            self.assertTrue(
                has_role(('LocalModerator', idea), elector))

    def test_vote_is_elector_gated(self):
        idea = self._reported_idea()
        self.request.user = self.carol
        self.assertIn('referendumprocess.vote', self._uids(idea))
        self.request.user = self.bob
        self.assertNotIn('referendumprocess.vote', self._uids(idea))
        self._vote(idea, self.carol, True)
        # one vote each: carol's action is gone, dave's remains
        self.request.user = self.carol
        self.assertNotIn('referendumprocess.vote', self._uids(idea))
        self.request.user = self.dave
        self.assertIn('referendumprocess.vote', self._uids(idea))

    def test_vote_requires_the_key(self):
        idea = self._reported_idea()
        self.request.user = self.carol
        self.assertRaises(KeyError, self._run, idea, 'vote', {})

    def test_majority_against_censors(self):
        idea = self._reported_idea()
        self._vote(idea, self.carol, False)
        self._vote(idea, self.dave, False)
        self._vote(idea, self.alice, True)
        self._decide(idea)
        self.assertEqual(idea.state, ['censored'])
        self.assertEqual(idea.reports[-1].state, ['processed'])
        # the verdict revokes the moderation grants
        for elector in self.electors:
            self.assertFalse(
                has_role(('LocalModerator', idea), elector))

    def test_majority_for_ignores(self):
        idea = self._reported_idea()
        for elector in self.electors:
            self._vote(idea, elector, True)
        self._decide(idea)
        self.assertNotIn('reported', idea.state)
        self.assertIn('published', idea.state)
        self.assertEqual(idea.reports[-1].state, ['processed'])

    def test_finished_ballot_blocks_re_reporting(self):
        idea = self._reported_idea()
        for elector in self.electors:
            self._vote(idea, elector, True)
        self._decide(idea)
        # the second half of the anti-re-report contract
        self.request.user = self.alice
        self.assertNotIn('reportsmanagement.report', self._uids(idea))
