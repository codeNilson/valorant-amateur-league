from django.db import models
from players.models import Player
from matches.models import Match


class Team(models.Model):
    uuid = models.UUIDField()
    players = models.ManyToManyField(
        Player, through="Stat", related_name="teams"
    )
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name="teams", null=True
    )

    def __str__(self):
        return self.players
