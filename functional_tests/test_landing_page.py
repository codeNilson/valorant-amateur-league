from django.urls import reverse
from selenium.webdriver.common.by import By
from .base import LavavaFunctionalTests


class LavavaLandingPageTests(LavavaFunctionalTests):

    def responsive_helper(self, width, height, callback):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(width, height)
        welcome_title = self.browser.find_element(
            By.XPATH, "/html/body/main/section[1]/div/div/div[2]"
        )
        welcome_title_position = welcome_title.value_of_css_property("position")
        return callback(welcome_title_position)

    def test_landing_page(self):
        # Acessa a página principal
        self.browser.get(self.live_server_url)

        # Testa se o título da página é o esperado
        self.assertIn("Valorant Amateur League", self.browser.title)

        # Testa o botão principal
        main_button = self.browser.find_element(By.ID, "mainButton")
        self.assertIn("Join the fun!", main_button.text)
        main_button.click()
        current_page = self.browser.current_url
        home_url = reverse("home")
        self.assertIn(home_url, current_page)

    def test_welcome_title_responsive_behavior(self):
        def welcome_title_position_is_absolute_if_width_less_than_768px(result):
            self.assertEqual("absolute", result)

        def welcome_title_position_is_static_if_width_768px(result):
            self.assertEqual("static", result)

        self.responsive_helper(
            783, 1024, welcome_title_position_is_absolute_if_width_less_than_768px
        )
        self.responsive_helper(
            784, 1024, welcome_title_position_is_static_if_width_768px
        )
