from django.test import LiveServerTestCase
from utils import get_browser


class LavavaFunctionalTests(LiveServerTestCase):
    def setUp(self):
        self.browser = get_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def set_windows_size(self, width, height):
        self.browser.set_window_size(width, height)