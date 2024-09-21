from django.db import models
from teams.models import Team
from gamedata.models import Agent


class Stat(models.Model):
    player = models.ForeignKey(
        "players.Player", on_delete=models.CASCADE, related_name="stats"
    )
    team = models.ForeignKey(
        "teams.Team",
        on_delete=models.SET_NULL,
        related_name="stats",
        null=True,
        blank=True,
    )
    agent = models.ForeignKey(
        "gamedata.Agent",
        on_delete=models.SET_NULL,
        related_name="stats",
        null=True,
        blank=True,
    )
    kills = models.PositiveIntegerField(null=True, blank=True)
    deaths = models.PositiveIntegerField(null=True, blank=True)
    assists = models.PositiveIntegerField(null=True, blank=True)
    mvp = models.BooleanField(null=True, blank=True)
    ace = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.player.username
