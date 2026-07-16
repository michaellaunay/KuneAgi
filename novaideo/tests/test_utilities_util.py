# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Unit tests of the pure vein of ``novaideo.utilities.util`` (T1b).

Characterisation tests, plain ``unittest``, no functional harness —
they run on both stacks. Pinned oddities of the current contract:

- ``combinaisons`` works on strings (concatenation-based);
- ``word_frequencies`` is a generator of ``(count, word)`` tuples;
- ``guess_extension`` answers without a dot for built-in types
  (``'png'``) but WITH the dot for custom-registered ones
  (``'.kat'``), and falls back to ``'file'``;
- ``get_files_data`` keeps images only;
- ``to_localized_time`` returns the *untranslated* ``${...}``
  templates when ``translate`` is false — the format-branch selection
  is thus fully deterministic — and unknown ``format_id`` raises
  ``KeyError``;
- ``truncate_text`` cuts mid-URL (no URL protection at this level).
"""
import datetime
import random
import unittest

import pytz
from pyramid.testing import DummyRequest

import novaideo.utilities.util as util


class Dummy(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)


class MathAndTextTests(unittest.TestCase):

    def test_factorielle(self):
        self.assertEqual(util.factorielle(0), 1)
        self.assertEqual(util.factorielle(5), 120)

    def test_combinaisons_concatenates_strings(self):
        # current contract: string elements, concatenation-based
        self.assertEqual(util.combinaisons(['a', 'b', 'c'], 3, 2),
                         ['abc'])

    def test_word_frequencies_is_a_generator_of_count_word(self):
        result = sorted(util.word_frequencies(
            'le chat et le chien et le chat', ['et']))
        self.assertEqual(result, [(1, 'chien'), (2, 'chat'), (3, 'le')])

    def test_extract_keywords(self):
        self.assertEqual(util.extract_keywords('Le grand chat noir'),
                         ['chat', 'grand', 'noir'])

    def test_normalize_title(self):
        # accents stripped, parentheses removed (double space kept),
        # non-ascii dashes dropped by the ascii-ignore encoding
        self.assertEqual(util.normalize_title('Économie (sociale) — Été'),
                         'economie sociale  ete')

    def test_truncate_text(self):
        self.assertEqual(util.truncate_text('bonjour tout le monde', 7),
                         'bonjour...')
        # no URL protection at this level: the cut lands mid-URL
        self.assertEqual(
            util.truncate_text('voir http://exemple.org/page longue', 12),
            'voir http://...')

    def test_get_url_domain(self):
        self.assertEqual(
            util.get_url_domain('https://www.exemple.org/a/b?c=1'),
            'https://www.exemple.org/')
        self.assertEqual(
            util.get_url_domain('https://www.exemple.org/a', True),
            'www.exemple.org')

    def test_gen_random_token_properties(self):
        # properties only: the exact stream is not part of the
        # contract across interpreter versions
        random.seed(42)
        first = util.gen_random_token()
        random.seed(42)
        second = util.gen_random_token()
        self.assertEqual(first, second)
        self.assertTrue(10 <= len(first) <= 15)
        self.assertTrue(first.isalnum())


class HtmlTests(unittest.TestCase):

    def test_html_to_text(self):
        self.assertEqual(
            util.html_to_text('<p>Bonjour <b>le</b> monde</p>'),
            'Bonjour le monde')

    def test_html_article_to_text_needs_its_structure(self):
        # these shapes are outside the expected article structure
        self.assertEqual(
            util.html_article_to_text('<div><h1>T</h1><p>Corps</p></div>'),
            '')
        self.assertEqual(
            util.html_article_to_text(
                '<article><h1>T</h1><p>Corps</p></article>'),
            '')


class FilesTests(unittest.TestCase):

    def test_guess_extension(self):
        # built-in type: no dot; unknown: 'file'
        self.assertEqual(
            util.guess_extension(Dummy(mimetype='image/png')), 'png')
        self.assertEqual(
            util.guess_extension(Dummy(mimetype='application/inexistant')),
            'file')

    def test_add_mimetype_map_answers_with_the_dot(self):
        util.add_mimetype_map('application/x-kuneagi-test', '.kat')
        self.assertEqual(
            util.guess_extension(
                Dummy(mimetype='application/x-kuneagi-test')),
            '.kat')

    def test_get_files_data_keeps_images_only(self):
        image = Dummy(mimetype='image/png', url='/f.png')
        document = Dummy(mimetype='application/pdf', url='/d.pdf')
        self.assertEqual(util.get_files_data([image]),
                         [{'content': '/f.png', 'type': 'img'}])
        self.assertEqual(util.get_files_data([document]), [])
        self.assertEqual(util.get_files_data([None]), [])


class LocalizedTimeTests(unittest.TestCase):

    def setUp(self):
        self.request = DummyRequest()
        self.request.get_time_zone = pytz.UTC
        self.date = datetime.datetime(2016, 7, 14, 15, 30,
                                      tzinfo=pytz.UTC)

    def test_digital_templates(self):
        # translate=False: the untranslated templates pin the
        # format-branch selection deterministically
        self.assertEqual(
            util.to_localized_time(self.date, request=self.request),
            '${day}/${month}/${year} ${hour}:${minute}')
        self.assertEqual(
            util.to_localized_time(self.date, request=self.request,
                                   date_only=True),
            '${day}/${month}/${year}')

    def test_defined_literal_template(self):
        self.assertEqual(
            util.to_localized_time(self.date, request=self.request,
                                   format_id='defined_literal'),
            "On ${day} ${month} ${year} at ${hour} o'clock"
            " and ${minute} minutes")

    def test_digital_ignores_the_ignore_flags(self):
        self.assertEqual(
            util.to_localized_time(self.date, request=self.request,
                                   ignore_year=True, add_day_name=True),
            '${day}/${month}/${year} ${hour}:${minute}')

    def test_unknown_format_raises(self):
        self.assertRaises(
            KeyError, util.to_localized_time, self.date,
            request=self.request, format_id='literal')


class TextUrlsFormatTests(unittest.TestCase):

    def test_wraps_urls_in_anchors(self):
        request = DummyRequest()
        result = util.text_urls_format('voir http://exemple.org/x ici',
                                       request=request)
        self.assertEqual(len(result), 4)
        all_urls, url_files, text_without, formatted = result
        self.assertEqual(all_urls, {})
        self.assertEqual(url_files, [])
        self.assertEqual(text_without, '<p></p>')
        self.assertIn('href="http://exemple.org/x"', formatted)
        self.assertIn('class="emoji-container"', formatted)
