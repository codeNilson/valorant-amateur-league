from .base import LavavaFunctionalTests
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LavavaNavbarTests(LavavaFunctionalTests):
    def setUp(self):

        super().setUp()

        # Acessa a página principal
        home_url = self.live_server_url + reverse("home")
        self.browser.get(home_url)

    def test_home_page_login_and_signup_buttons(self):
        # Testa se os botões de login e signup aparecem se o usuário não estiver logado
        login_button = self.browser.find_element(
            By.XPATH, "//*[@id='navbarSupportedContent']/ul[2]/li[1]/a"
        )
        signup_button = self.browser.find_element(
            By.XPATH, "//*[@id='navbarSupportedContent']/ul[2]/li[2]/a"
        )

        self.assertIsNotNone(login_button)
        self.assertIsNotNone(signup_button)
