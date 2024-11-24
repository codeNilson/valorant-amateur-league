import random
import os
import requests
from dotenv import load_dotenv
from django.utils import timezone

load_dotenv()


def get_random_color() -> int:
    cores_decimais = [
        65535,  # Ciano (0x00FFFF)
        255,  # Azul (0x0000FF)
        16711935,  # Rosa choque (0xFF00FF)
        16776960,  # Amarelo (0xFFFF00)
        65280,  # Verde (0x00FF00)
        16711680,  # Vermelho (0xFF0000)
    ]
    return random.choice(cores_decimais)


class DiscordWebhook:
    def __init__(self, webhook_url=None):
        self.webhook_url = webhook_url or os.environ.get("DISCORD_WEBHOOK")

    def send_ranking_update(self, players):

        rankings = "\n".join(f"#{i + 1}" for i in range(len(players)))
        usernames = "\n".join(player.username for player in players)
        points = "\n".join(str(player.points) for player in players)

        embed = {
            "title": "Veja no nosso site!",
            "url": "http://localhost:8000/home/",
            "color": get_random_color(),
            "author": {
                "name": "Nova atualiazação!",
                "url": "https://lavava.com.br",
                "icon_url": "https://i.pinimg.com/736x/0e/7d/a4/0e7da4a80ec2a70257a5537510455ea5.jpg",
            },
            "fields": [
                {
                    "name": "Ranking",
                    "value": rankings,
                    "inline": True,
                },
                {
                    "name": "Jogador",
                    "value": usernames,
                    "inline": True,
                },
                {
                    "name": "Pontos",
                    "value": points,
                    "inline": True,
                },
            ],
            "footer": {"text": "Última atualização"},
            "timestamp": timezone.now().isoformat(),
            "thumbnail": {"url": "https://img.icons8.com/color/512/valorant.png"},
        }

        requests.post(
            self.webhook_url,
            timeout=10,
            json={
                "content": "<@&1309639892791332905>\n# Tabela atualizada!\nVejam os novos rankings!",
                "embeds": [embed],
                "attachments": [],
            },
        )
