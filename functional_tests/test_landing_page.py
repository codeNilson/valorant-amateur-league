from django.urls import reverse
from selenium.webdriver.common.by import By
from .base import LavavaFunctionalTests


class LavavaLandingPageTests(LavavaFunctionalTests):

    def test_landing_page(self):
        # Acessa a página principal
        self.browser.get(self.live_server_url)

        # Testa se o título da página é o esperado
        self.assertEqual("Valorant Amateur League", self.browser.title)

        # Testa o botão principal
        main_button = self.browser.find_element(By.ID, "mainButton")
        self.assertEqual("Join the fun!", main_button.text)
        main_button.click()
        current_page = self.browser.current_url
        home_url = reverse("home")
        self.assertEqual(self.live_server_url + home_url, current_page)

    def test_welcome_title_position_is_absolute_if_width_less_than_768px(self):

        def callback(result):
            self.assertEqual("absolute", result)

        self.responsive_helper(783, callback)

    def test_welcome_title_position_is_static_if_width_768px(self):

        def callback(result):
            self.assertEqual("static", result)

        self.responsive_helper(784, callback)
