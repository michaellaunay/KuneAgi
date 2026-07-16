# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Unit tests of the pure helpers of ``novaideo.utilities.pseudo_react``
(T1b — the metadata composers need the functional harness and belong
to a later batch).
"""
import unittest

# pseudo_react and novaideo.views import each other; the application
# resolves the cycle through its scan order — prime it the same way:
import novaideo.views  # noqa: F401
from novaideo.utilities import pseudo_react


class DummyRequest(object):
    def static_url(self, source):
        return 'http://ex/' + source


class PseudoReactHelpersTests(unittest.TestCase):

    def test_get_components_data_injects_action_id(self):
        self.assertEqual(
            pseudo_react.get_components_data('my-action', None, a=1),
            {'a': 1, 'action_id': 'my-action'})

    def test_get_resources_to_include(self):
        resources = {'css_links': ['a.css', 'b.css'],
                     'js_links': ['a.js', 'a.css']}
        currents = ['http://ex/b.css']
        result = pseudo_react._get_resources_to_include(
            DummyRequest(), resources, currents)
        # typed, deduplicated against currents and against itself
        self.assertEqual(result,
                         ['css@http://ex/a.css',
                          'js@http://ex/a.js',
                          'js@http://ex/a.css'])
        self.assertEqual(
            pseudo_react._get_resources_to_include(DummyRequest(), {}, []),
            [])
