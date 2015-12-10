from django.conf import settings

from faker import Faker
from selenium.common.exceptions import NoSuchElementException

from briansdojo.models import Project
from briansdojo.selenium_test import SeleniumTestCase


class TestBriansDojo(SeleniumTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestBriansDojo, cls).setUpClass()
        cls.browser.get(settings.BASE_URL)

        # Add some fake data
        cls.fake = Faker()
        for i in range(4):
            Project.objects.create(
                title=cls.fake.company(),
                description=cls.fake.text(),
                url=cls.fake.url(),
                image='briansdojo/project/%s' % cls.fake.file_name(extension='jpg')
            )

    def test_homepage_title(self):
        self.assertEqual(self.browser.title, "Brian's Dojo")

    def test_homepage_sections(self):
        self.assertEqual(
            len(self.browser.find_elements_by_css_selector('#main > section')),
            4
        )

        self.assertRaises(
            NoSuchElementException,
            self.browser.find_element_by_css_selector,
            '#noident'
        )

    def test_contact_form(self):
        sender_input = self.browser.find_element_by_id('id_sender')
        email_input = self.browser.find_element_by_id('id_email')
        message_input = self.browser.find_element_by_id('id_message')
        form_submit = self.browser.find_element_by_id('submit_contact_home')

        sender_input.send_keys(self.fake.name())
        email_input.send_keys(self.fake.safe_email())
        message_input.send_keys(self.fake.text())

        form_submit.click()

        self.assertTrue(self.browser.find_element_by_id('contact_success'))
        self.assertEqual(
            self.browser.find_element_by_id('contact_success').text,
            "Thanks, your message has been sent. I'll be in touch shortly."
        )
