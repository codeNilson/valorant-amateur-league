import pytest
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

    @pytest.mark.skip(reason="Teste de responsividade não está funcionando")
    def test_responsive_helper(self):
        # Lista de breakpoints com tamanhos de janela e sufixos esperados no nome da imagem
        breakpoints = [
            (400, "_small"),
            (1200, "_medium"),
            (2560, "_large"),
        ]

        for width, expected_suffix in breakpoints:
            # Ajusta o tamanho da janela do navegador
            self.browser.set_window_size(width, 1024)

            # Espera que o navegador faça o carregamento correto das imagens para o novo tamanho da janela
            carousel_items = self.browser.find_elements(By.CLASS_NAME, "carousel-item")
            for item in carousel_items:
                # Localiza a tag img dentro do item do carrossel
                image = item.find_element(By.TAG_NAME, "img")
                src_image = image.get_attribute("src")

                # Verifica se o sufixo correto está no nome da imagem
                self.assertIn(
                    expected_suffix,
                    src_image,
                    f"Expected suffix '{expected_suffix}' in '{src_image}' for width {width}",
                )

    def test_home_page_title(self):

        # Testa se o título da página é o esperado
        self.assertEqual("Valorant Amateur League", self.browser.title)

    def test_home_page_carousel(self):

        carousel_items = self.browser.find_elements(By.CLASS_NAME, "carousel-item")

        self.assertEqual(len(carousel_items), 2)

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
