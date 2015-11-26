from briansdojo.selenium_test import SeleniumTestCase


class TestBriansDojo(SeleniumTestCase):
    def test_page_title(self):
        self.browser.get('http://briansdojo.co.uk')
        self.assertEqual(self.browser.title, "Brian's Dojo")
