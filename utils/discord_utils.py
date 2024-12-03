from dataclasses import dataclass, field
import random
import os
from typing import Optional
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
                "name": "Nova atualização!",
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


widget = requests.get(
    "https://discord.com/api/guilds/1243610772064698398/widget.json", timeout=10
).json()


@dataclass
class DiscordMember:
    id: str
    username: str
    status: str
    avatar_url: str
    channel_id: Optional[str] = None


@dataclass
class DiscordChannel:
    id: str
    name: str
    position: int
    members: list[DiscordMember] = field(default_factory=list)

    def add_member(self, member: "DiscordMember"):
        self.members.append(member)


@dataclass
class DiscordWidget:
    id: str
    name: str
    instant_invite: str
    presence_count: int
    channels: list[DiscordChannel] = field(default_factory=list)
    members: list[DiscordMember] = field(default_factory=list)

    @classmethod
    def create_from_json(cls, widget_json):
        channels = []

        for channel in widget_json["channels"]:
            discord_channel = DiscordChannel(
                id=channel["id"],
                name=channel["name"],
                position=channel["position"],
            )
            channels.append(discord_channel)
        channels.sort(key=lambda c: c.position)

        members = []

        for member in widget_json["members"]:
            discord_member = DiscordMember(
                id=member.get("id"),
                username=member.get("username"),
                status=member.get("status"),
                avatar_url=member.get("avatar_url"),
                channel_id=member.get("channel_id"),
            )
            for channel in channels:
                if channel.id == discord_member.channel_id:
                    channel.add_member(discord_member)
                    break

            members.append(discord_member)

        widget_id = widget_json["id"]
        name = widget_json["name"]
        instant_invite = widget_json["instant_invite"]
        presence_count = widget_json["presence_count"]

        return cls(
            id=widget_id,
            name=name,
            instant_invite=instant_invite,
            presence_count=presence_count,
            channels=channels,
            members=members,
        )
