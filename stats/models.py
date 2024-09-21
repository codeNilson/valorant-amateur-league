from django.db import models
from players.models import Player
from teams.models import Team
from gamedata.models import Agent
from matches.models import Match


class Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="stats")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="stats")
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, related_name="stats", null=True
    )
    kills = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    mvp = models.BooleanField(null=True)
    ace = models.BooleanField(null=True)
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name="stats", null=True
    )

    def __str__(self):
        return self.player
