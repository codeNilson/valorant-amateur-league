from django.db import models
import uuid


class Team(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    players = models.ManyToManyField(
        "players.Player", through="stats.Stat", related_name="teams"
    )
    match = models.ForeignKey(
        "matches.Match",
        on_delete=models.SET_NULL,
        related_name="teams",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.uuid)
