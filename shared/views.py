import os
import requests
from PIL import Image
from io import BytesIO
from django.views import View
from django.http import HttpResponse
from django.conf import settings

# from django.shortcuts import render


class SaveImages:
    def __init__(
        self,
        list_images,
        path,
        quality=100,
        optimize=True,
        images_extension="webp",
        timeout=5,
    ):
        """
        Inicializa a classe SaveImages.

        :param maps: Lista de URLs das imagens.
        :param path: Caminho onde as imagens serão salvas.
        :param quality: Qualidade da imagem (1-100).
        :param optimize: Se deve otimizar a imagem ao salvar.
        :param images_extension: Extensão das imagens salvas.
        :param timeout: Tempo limite para requisições.
        """
        self.list_images = list_images
        self.path = path
        self.quality = quality
        self.optimize = optimize
        self.images_extension = images_extension
        self.timeout = timeout
        self.images = []

        os.makedirs(self.path, exist_ok=True)

    def request_urls(self):
        """Faz requisições para as URLs das imagens e armazena as imagens na lista."""
        for agent in self.list_images:
            try:
                image_response = requests.get(
                    agent["background"], timeout=self.timeout
                )
                image_response.raise_for_status()
                image = Image.open(BytesIO(image_response.content))
                self.images.append({"image": image, "name": agent["displayName"]})
            except (requests.RequestException, IOError) as e:
                print(f"Erro ao baixar a imagem de {agent["background"]}: {e}")

    def save_images(self):
        """Salva as imagens no diretório especificado."""
        for image in self.images:

            filename = (
                image["name"]
                .lower()
                .replace(" ", "_")
                .replace("-", "_")
                .replace("/", "_")
                + "_background"
            )

            file_path = os.path.join(self.path, f"{filename}.{self.images_extension}")
            if not os.path.exists(file_path):
                image["image"].save(
                    file_path,
                    format=self.images_extension or image.format,
                    quality=self.quality,
                    optimize=self.optimize,
                )
                print(f"Imagem salva: {file_path}")
            else:
                print(f"Imagem já existe: {file_path}")


class MapsView(View):
    def get(self, request):

        # URL da API
        api_url = "https://valorant-api.com/v1/maps"

        # Requisição
        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()  # Levanta um erro para respostas de erro
            json_data = response.json()["data"]

            mapas = [
                mapa
                for mapa in json_data
                if mapa["displayName"].lower()
                not in (
                    "drift",
                    "glitch",
                    "piazza",
                    "basic training",
                    "the range",
                    "district",
                )
            ]

            saver = SaveImages(
                maps=mapas,
                path=settings.MEDIA_ROOT / "maps/vertical_icons/",
                quality=80,
                optimize=True,
                images_extension="webp",
            )

            saver.request_urls()
            saver.save_images()

        except requests.RequestException as e:
            print(f"Erro ao acessar a API: {e}")

        return HttpResponse("This is the shared view.")


class AgentsView(View):
    def get(self, request):

        # URL da API
        api_url = "https://valorant-api.com/v1/agents?isPlayableCharacter=True"

        # Requisição
        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()  # Levanta um erro para respostas de erro
            json_data = response.json()["data"]

            agents = [agent for agent in json_data]

            saver = SaveImages(
                list_images=agents,
                path=settings.MEDIA_ROOT / "agents/backgrounds/",
                quality=80,
                optimize=True,
                images_extension="webp",
            )

            saver.request_urls()
            saver.save_images()

        except requests.RequestException as e:
            print(f"Erro ao acessar a API: {e}")

        return HttpResponse("This is the shared view.")
