from novaideo.testing import FunctionalTests
from novaideo.utilities.text_analyzer import ITextAnalyzer
from pyramid.threadlocal import get_current_registry


class TestTextAnalyzerIntegration(FunctionalTests):

    def setUp(self):
        super(TestTextAnalyzerIntegration, self).setUp()

    def _include_spanids(self, spanids, todel, toins, soup):
        spanids_data = []
        for spanid in spanids:
            spanid_data = {'tag': spanid,
                                'todel': todel,
                                'toins': toins,
                                'blocstodel': None
                                }
            spanids_data.append(spanid_data)
        return spanids_data

    def list_all_spans(self, identifier, soup):
        all_id_spans = soup.find_all('span',{'id': identifier})
        spans_list = [tag for tag in all_id_spans]
        return spans_list

    def unwrap_spans(self, span_id, decision):
        if span_id == 'diffid' or decision == 'accept_modif':
            spans_list = self.list_all_spans(span_id, self.soup_wrapped)
            spanids_data = self._include_spanids(spans_list, "del", "ins", self.soup_wrapped)
            self.text_analyzer.unwrap_diff(spanids_data, self.soup_wrapped)

        elif decision == 'refuse_modif':
            spans_list = self.list_all_spans(span_id, self.soup_wrapped)
            spanids_data = self._include_spanids(spans_list, "ins", "del", self.soup_wrapped)
            self.text_analyzer.unwrap_diff(spanids_data, self.soup_wrapped)

    def entry_to_result(self, text1, text2, decision):
        self.text_analyzer = get_current_registry().getUtility(ITextAnalyzer,'text_analyzer')
        souptextdiff, textdiff = self.text_analyzer.render_html_diff(text1, text2)
        self.soup_wrapped = self.text_analyzer.wrap_diff(textdiff, 'modif')
        self.unwrap_spans('modif', decision)
        self.unwrap_spans('diffid', None)
        soup_to_text = self.text_analyzer.soup_to_text(self.soup_wrapped)
        return soup_to_text

    def assert_text(self, results):
        for result in results:
            self.assertNotIn("&nbsp", result)
            self.assertNotIn("\xa0", result)
            self.assertNotIn("  ", result)

    def test_full_process_result(self):
        results=[]
        #deletion
        text1 = "<p>Organisation !</p>"
        text2 = "<p>Organisation</p>"
        result1 = self.entry_to_result(text1, text2, 'accept_modif')
        results.append(result1)
        self.assertEqual(result1,'<p>Organisation</p>')
        #insertion
        text3 = "<p>Organisation</p>"
        text4 = "<p>Organisation !</p>"
        result2 = self.entry_to_result(text3, text4, 'refuse_modif')
        results.append(result2)
        self.assertEqual(result2,'<p>Organisation</p>')
        #replacement
        text5 = "<p>Organisation&nbsp!</p>"
        text6 = "<p>Organisation de conferences\xa0?</p>"
        result3 = self.entry_to_result(text5, text6, 'accept_modif')
        results.append(result3)
        self.assertEqual(result3,'<p>Organisation de conferences ?</p>')
        self.assert_text(results)
