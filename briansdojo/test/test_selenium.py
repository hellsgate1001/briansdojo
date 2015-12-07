from django.conf import settings

from briansdojo.selenium_test import SeleniumTestCase


class TestBriansDojo(SeleniumTestCase):
    def test_homepage_title(self):
        self.browser.get(settings.BASE_URL)
        self.assertEqual(self.browser.title, "Brian's Dojo")
