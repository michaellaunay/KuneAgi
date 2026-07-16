# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Unit tests of ``novaideo.utilities.french_dates_parser`` (T1).

Characterisation tests: they pin the parser's *current* contract,
observed under the module's own frozen reference date
(``mockLocalTime``: 2006-05-15). Notable pinned facts:

- the sentence anchor is the CAPITALISED article: ``Du .. au ..`` and
  ``Le ..`` parse; the lowercase forms return ``None``;
- explicit years inside ``Du .. au ..`` are not part of the grammar
  (the year comes from the reference time);
- ``getRangJour`` captures the day, not the rank, in its current form;
- the historical header bug ("Il ne devrait pas y avoir le 1er
  mardi") is exercised at this level through the bounds it produces —
  its visible symptom is pinned in ``test_ical_date_utility``.

Runs on both stacks (plain ``unittest``, no functional harness).
"""
import unittest

import novaideo.utilities.french_dates_parser as parser


class FrenchDatesParserTests(unittest.TestCase):

    def setUp(self):
        self._local_time = parser.getLocalTime
        parser.getLocalTime = parser.mockLocalTime      # 2006-05-15

    def tearDown(self):
        parser.getLocalTime = self._local_time

    def test_reference_and_date_math(self):
        # None -> the frozen reference, as [Y, M, D, weekday, rank]
        self.assertEqual(parser.getDateAMJNR(None), [2006, 5, 15, 0, 3])
        # explicit date: weekday and month-rank are computed
        self.assertEqual(parser.getDateAMJNR([2016, 7, 14]),
                         [2016, 7, 14, 3, 2])
        # day increment rolls the year over
        self.assertEqual(parser.incJour([2016, 12, 31, 5, 5]),
                         [2017, 1, 1, 6, 1])

    def test_hours_extraction(self):
        table = [
            # compact 'NNh[MM]' forms parse; (start, end) pairs
            ('de 14h à 18h30', [[14, None], [18, 30]]),
            # spelled-out and spaced forms are outside the grammar
            ('à 20 heures 15', []),
            ('de 9 h à 12 h et de 14 h à 17 h', []),
        ]
        for phrase, expected in table:
            self.assertEqual(
                parser.getTimeDeExpHeuresMinutes(phrase), expected, phrase)

    def test_day_and_rank(self):
        table = [
            # current contract: the day index is captured, the rank
            # ('premier', 'deuxième'...) is not
            ('le premier mardi', [[1, None]]),
            ('les deuxième et quatrième jeudis', [[3, None]]),
            ('tous les lundis', [[0, None]]),
        ]
        for phrase, expected in table:
            self.assertEqual(parser.getRangJour(phrase), expected, phrase)

    def test_day_ranges(self):
        # first element only: the second carries spans and compiled
        # regexes (implementation detail)
        self.assertEqual(
            parser.getJoursDeExpNomJour('du lundi au vendredi')[0],
            [[0, 4]])
        self.assertEqual(
            parser.getJoursDeExpNomJour('le mardi et le jeudi')[0], [])
        self.assertEqual(
            parser.getJoursDeExpNomJour('tous les jours')[0], [])

    def test_hours_of_seances(self):
        result = parser.getHeuresDeExpHeureSeances(
            'du lundi au vendredi de 14h à 18h')
        self.assertEqual(result[0], [[[14, None], [18, None]]])

    def test_closed_days(self):
        # 'fermé le <jour>' yields a day-only closure entry
        self.assertEqual(parser.getJoursFermes('fermé le lundi'),
                         [[None, None, None, 0, None]])
        # the 'sauf ...' clause alone is not a closure at this level
        self.assertEqual(
            parser.getJoursFermes('sauf le mardi et les jours fériés'), [])

    def test_periode_expansion(self):
        self.assertEqual(
            parser.getDatesFromPeriode([2016, 6, 14], [2016, 6, 20]),
            [[2016, 6, 14, 1, 2], [2016, 6, 15, 2, 3], [2016, 6, 16, 3, 3],
             [2016, 6, 17, 4, 3], [2016, 6, 18, 5, 3], [2016, 6, 19, 6, 3],
             [2016, 6, 20, 0, 3]])

    def test_checkDates_passthrough(self):
        dates = [[2016, 3, 4, 4, 1]]
        self.assertEqual(parser.checkDates(dates), dates)

    def test_orchestrator_grammar(self):
        seances_9_12 = [[[9, None], [12, None]]]
        table = [
            # the capitalised article anchors the sentence
            ('Du 3 au 5 mars de 9h à 12h',
             [[2006, 3, 3, seances_9_12], [2006, 3, 5, seances_9_12]]),
            ('Du 3 mars au 5 mars de 9h à 12h',
             [[2006, 3, 3, seances_9_12], [2006, 3, 5, seances_9_12]]),
            ('Du 14 juin au 21 juillet de 14h à 18h',
             [[2006, 6, 14, [[[14, None], [18, None]]]],
              [2006, 7, 21, [[[14, None], [18, None]]]]]),
            ('Le 15 janvier à 14h',
             [[2006, 1, 15, [[[14, None], None]]]]),
            # lowercase forms are outside the grammar
            ('du 3 au 5 mars de 9h à 12h', None),
            ('le 15 janvier à 14h', None),
        ]
        for phrase, expected in table:
            self.assertEqual(
                parser.getDatesFromSeances(phrase), expected, phrase)

    def test_historical_header_bounds(self):
        """The module-header bug phrase parses to its 2006 bounds."""
        phrase = ('Du 14 juin au 21 juillet du lundi au dimanche '
                  'de 14h à 18h, sauf le mardi et les jours fériés')
        self.assertEqual(
            parser.getDatesFromSeances(phrase),
            [[2006, 6, 14, [[[14, None], [18, None]]]],
             [2006, 7, 21, [[[14, None], [18, None]]]]])
