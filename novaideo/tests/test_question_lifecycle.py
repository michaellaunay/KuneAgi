# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Question-process lifecycle (T4, first slice).

Behaviour-level characterisation of ``question_management`` — the
largest untested rule set (1 049 lines). Pinned contracts:

- ``creat`` publishes immediately with the DUAL state
  ``['pending', 'published']``;
- the role gates are exact: the author/admin extras on a published
  question are ``{edit, archive, seehistory}``; on someone else's
  answer the admin extra is ``{archive}`` alone (the author edits her
  own answer);
- answering raises one alert AT THE ROOT (the alert store is central,
  not per-user);
- supporting a question consumes NO personal token, flips
  ``support`` to ``withdraw_token`` (oppose stays), and withdrawing
  restores it symmetrically;
- VALIDATING an answer closes the question — the cross-object cascade
  ``answer: ['validated', 'published']`` /
  ``question: ['closed', 'published']``;
- ``archive`` REQUIRES an ``explanation`` (KeyError without), moves to
  ``['archived']``, alerts the root store, and collapses the gates:
  members keep NO action, the admin keeps the quintet with
  ``delquestion`` appearing.
"""
from dace.util import getAllBusinessAction

from novaideo.testing import FunctionalTests
from novaideo.content.question import Question, Answer
from novaideo.tests.example.app import add_user


class TestQuestionLifecycle(FunctionalTests):

    def setUp(self):
        super(TestQuestionLifecycle, self).setUp()
        self.default_novaideo_config()
        self.root = self.request.root
        self.admin = self.request.user
        question = Question(title='Question title', text='Question text',
                            keywords=['k1'])
        self._run(self.root, 'creat', {'_object_data': question},
                  'questionmanagement')
        self.question = self.root.questions[-1]

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

    def _alice(self):
        alice = add_user({'first_name': 'Alice', 'last_name': 'A',
                          'email': 'alice@example.com',
                          'password': 'alice'}, self.request)
        self.request.user = alice
        return alice

    def _answer(self):
        answer = Answer(comment='The answer', intention='Remark')
        self._run(self.question, 'answer', {'_object_data': answer})
        return self.question.answers[-1]

    # --- creation ------------------------------------------------------

    def test_creat_state_and_shape(self):
        self.assertEqual(self.question.state, ['pending', 'published'])
        self.assertIs(self.question.author, self.admin)
        self.assertEqual(len(self.question.channels), 1)
        self.assertEqual(len(self.question.answers), 0)

    def test_role_gates_on_published(self):
        admin_set = self._uids(self.question)
        self.assertEqual(admin_set, {
            'novaideoabstractprocess.select',
            'novaideoviewmanager.seehistory',
            'questionmanagement.answer', 'questionmanagement.archive',
            'questionmanagement.associate', 'questionmanagement.comment',
            'questionmanagement.edit', 'questionmanagement.oppose',
            'questionmanagement.present', 'questionmanagement.see',
            'questionmanagement.support', 'reportsmanagement.report'})
        self._alice()
        # a plain member loses exactly the author/admin extras
        self.assertEqual(
            admin_set - self._uids(self.question),
            {'questionmanagement.edit', 'questionmanagement.archive',
             'novaideoviewmanager.seehistory'})

    # --- answering -----------------------------------------------------

    def test_answer_execution_and_alert(self):
        alerts_before = len(self.root.alerts)
        alice = self._alice()
        answer = self._answer()
        self.assertEqual(len(self.question.answers), 1)
        self.assertEqual(answer.state, ['published'])
        self.assertIs(answer.author, alice)
        # one alert lands in the CENTRAL store
        self.assertEqual(len(self.root.alerts), alerts_before + 1)

    def test_answer_role_gates(self):
        self._alice()
        answer = self._answer()
        alice_set = self._uids(answer)
        self.assertEqual(alice_set, {
            'answermanagement.associate', 'answermanagement.comment',
            'answermanagement.edit', 'answermanagement.oppose',
            'answermanagement.present', 'answermanagement.see',
            'answermanagement.support',
            'answermanagement.transformtoidea',
            'answermanagement.validate',
            'ideamanagement.creatandpublish',
            'ideamanagement.creatandpublishasproposal',
            'reportsmanagement.report'})
        self.request.user = self.admin
        # the admin extra on someone else's answer: archive alone
        self.assertEqual(self._uids(answer) - alice_set,
                         {'answermanagement.archive'})

    # --- support tokens ------------------------------------------------

    def test_support_moves_the_gate_without_tokens(self):
        alice = self._alice()
        self._run(self.question, 'support', {})
        self.assertEqual(self.question.len_support, 1)
        # question support consumes no personal token
        self.assertEqual(len(getattr(alice, 'tokens', [])), 0)
        uids = self._uids(self.question)
        self.assertNotIn('questionmanagement.support', uids)
        self.assertIn('questionmanagement.withdraw_token', uids)
        self.assertIn('questionmanagement.oppose', uids)

    def test_withdraw_token_symmetry(self):
        self._alice()
        self._run(self.question, 'support', {})
        self._run(self.question, 'withdraw_token', {})
        self.assertEqual(self.question.len_support, 0)
        self.assertIn('questionmanagement.support',
                      self._uids(self.question))

    # --- validation cascade --------------------------------------------

    def test_validate_answer_closes_the_question(self):
        self._alice()
        answer = self._answer()
        self.request.user = self.admin
        self._run(answer, 'validate', {})
        self.assertEqual(answer.state, ['validated', 'published'])
        self.assertEqual(self.question.state, ['closed', 'published'])

    # --- archiving -----------------------------------------------------

    def test_archive_requires_an_explanation(self):
        self.assertRaises(KeyError, self._run,
                          self.question, 'archive', {})
        alerts_before = len(self.root.alerts)
        self._run(self.question, 'archive',
                  {'explanation': 'Duplicate question'})
        self.assertEqual(self.question.state, ['archived'])
        self.assertEqual(len(self.root.alerts), alerts_before + 1)

    def test_archived_gates_collapse(self):
        self._run(self.question, 'archive',
                  {'explanation': 'Duplicate question'})
        self.assertEqual(self._uids(self.question), {
            'novaideoviewmanager.seehistory',
            'questionmanagement.archive',
            'questionmanagement.associate',
            'questionmanagement.delquestion',
            'questionmanagement.see'})
        self._alice()
        self.assertEqual(self._uids(self.question), set())
