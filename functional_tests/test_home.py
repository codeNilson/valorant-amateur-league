from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base import LavavaFunctionalTests


class LavavaHomeTests(LavavaFunctionalTests):

    def setUp(self):

        super().setUp()

        # Acessa a home page
        home_url = self.live_server_url + reverse("home")
        self.browser.get(home_url)

    def test_home_page_title(self):

        # Testa se o título da página é o esperado
        self.assertEqual("Valorant Amateur League", self.browser.title)

    def teste_home_page_update_button_do_show_if_user_not_logged(self):
        # Testa se o botão de atualizar tabela não aparece se o usuário não estiver logado
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element(By.ID, "updateButton")

    def test_home_page_update_button_do_show_if_user_is_staff(self):
        # Testa se o botão de atualizar tabela aparece se o usuário estiver logado
        self.login_user("teste@teste.com", "testpassword")

        update_button = self.browser.find_element(By.ID, "updateButton")
        self.assertIsNotNone(update_button)

    def test_home_page_update_button_do_not_show_if_user_is_not_staff(self):
        # Testa se o botão de atualizar tabela não aparece caso usuário não seja staff
        self.player.is_staff = False
        self.player.save()

        self.login_user(
            "teste@teste.com",
            "testpassword",
        )

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element(By.ID, "updateButton")
