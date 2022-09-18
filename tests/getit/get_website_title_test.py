import unittest

from getit.get_website_title import get_title_from_website


class GetItWebsiteTitleTestCase(unittest.TestCase):

    def test_should_get_title_from_google_result_successful(self):
        (status, title) = get_title_from_website('https://google.com')
        self.assertEqual(status, 200)
        self.assertEqual(title, 'Before you continue to Google Search')

    def test_should_get_title_from_ddg_result_successful(self):
        (status, title) = get_title_from_website('https://duckduckgo.com')
        self.assertEqual(status, 200)
        self.assertEqual(title, 'DuckDuckGo — Privacy, simplified.')


if __name__ == '__main__':
    unittest.main()
