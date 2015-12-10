from django.test import TestCase

from pyvirtualdisplay import Display
from selenium import webdriver


class SeleniumTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.display = Display(visible=0, size=(1440, 900))
        cls.display.start()

        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        cls.display.stop()
