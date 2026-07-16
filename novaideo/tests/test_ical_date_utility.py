# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Unit tests of ``novaideo.utilities.ical_date_utility`` (T1).

Characterisation under the parser's frozen reference (2006-05-15).
The layer memoizes on the ``context`` argument, so any plain object
works as context (``None`` does not: the memoizer needs ``setattr``).

``test_header_bug_opening_day_escapes_sauf`` pins the bug documented
in the parser's own header since 2006 ("Il ne devrait pas y avoir le
1er mardi !") — refined by this very test run: the exclusion works for
every occurrence EXCEPT the period's opening day. The 2016 repro
started on a Tuesday; under the 2006 reference, a period opening on
Tuesday 2006-06-20 shows the same symptom. The assertions encode the
current, buggy behaviour on purpose — fixing the parser must flip them
consciously.
"""
import datetime
import unittest

import novaideo.utilities.french_dates_parser as parser
import novaideo.utilities.ical_date_utility as ical


class DummyContext(object):
    """Bare object: the memoizer stores its cache on the instance."""


class IcalDateUtilityTests(unittest.TestCase):

    def setUp(self):
        self._local_time = parser.getLocalTime
        parser.getLocalTime = parser.mockLocalTime      # 2006-05-15

    def tearDown(self):
        parser.getLocalTime = self._local_time

    def test_getDatesFromString_bounds(self):
        seances = [[[9, None], [12, None]]]
        self.assertEqual(
            ical.getDatesFromString(DummyContext(),
                                    'Du 3 au 5 mars de 9h à 12h'),
            [[2006, 3, 3, seances], [2006, 3, 5, seances]])

    def test_set_recurrence_expands_the_period(self):
        phrase = 'Du 3 au 5 mars de 9h à 12h'
        dates = ical.getDatesFromString(DummyContext(), phrase)
        self.assertEqual(
            ical.set_recurrence(dates, phrase),
            'RDATE;VALUE=DATE-TIME:'
            '20060303T000000,20060304T000000,20060305T000000')

    def test_sauf_excludes_the_weekday(self):
        """'sauf le mardi': every Tuesday inside the period is excluded."""
        phrase = ('Du 14 juin au 21 juillet du lundi au dimanche '
                  'de 14h à 18h, sauf le mardi et les jours fériés')
        dates = ical.getDatesFromString(DummyContext(), phrase)
        rdate = ical.set_recurrence(dates, phrase)
        self.assertIn('20060614T', rdate)       # Wednesday, opens, kept
        for tuesday in ('20060620T', '20060627T', '20060704T',
                        '20060711T', '20060718T'):
            self.assertNotIn(tuesday, rdate)

    def test_header_bug_boundary_days_escape_sauf(self):
        """Both BOUNDARY days bypass the 'sauf' filter (the 2006 bug).

        Opening on Tuesday 2006-06-20 and closing on Tuesday
        2006-07-04, with 'sauf le mardi': the interior Tuesday
        (2006-06-27) is excluded as specified, but BOTH boundaries are
        kept. The 2016 header repro only exposed the opening half —
        its closing day was a Thursday. Pinned as-is; fixing the
        parser must flip these consciously.
        """
        phrase = ('Du 20 juin au 4 juillet du lundi au dimanche '
                  'de 14h à 18h, sauf le mardi et les jours fériés')
        dates = ical.getDatesFromString(DummyContext(), phrase)
        rdate = ical.set_recurrence(dates, phrase)
        self.assertIn('20060620T', rdate)       # opening boundary: kept
        self.assertNotIn('20060627T', rdate)    # interior: excluded
        self.assertIn('20060704T', rdate)       # closing boundary: kept

    def test_getMiseAJourSeance_rebases_the_phrase(self):
        self.assertEqual(
            ical.getMiseAJourSeance('Du 3 au 5 mars de 9h à 12h',
                                    datetime.datetime(2006, 3, 4),
                                    context=DummyContext()),
            ("Jusqu'au 5 mars de 9h à 12h", None))

    def test_occurences_until_and_from(self):
        # ``is_ints`` means the dates are integer timestamps; the
        # deterministic path is datetimes. Both helpers are lazy
        # (itertools): materialise to compare.
        dates = [datetime.datetime(2006, 3, 3, 9, 0),
                 datetime.datetime(2006, 3, 4, 9, 0),
                 datetime.datetime(2006, 3, 5, 9, 0)]
        until = datetime.datetime(2006, 3, 4)
        kept = list(ical.occurences_until(until, list(dates)))
        self.assertEqual(kept, [datetime.datetime(2006, 3, 3, 9, 0)])
        from_ = datetime.datetime(2006, 3, 4)
        kept = list(ical.occurences_from(from_, list(dates)))
        self.assertEqual(kept, [datetime.datetime(2006, 3, 4, 9, 0),
                                datetime.datetime(2006, 3, 5, 9, 0)])
