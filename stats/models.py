from django.db import models
from django.forms import ValidationError


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
    mvp = models.BooleanField(null=True, default=False)
    ace = models.BooleanField(null=True, default=False)

    class Meta:
        unique_together = ("player", "team")

    def get_kda(self):
        """Calculates the KDA of the player."""
        try:
            kda = self.kills + self.assists / self.deaths
        except ZeroDivisionError:
            kda = self.kills + self.assists
        return kda

    def clean_players(self):
        """Checks if the team already has five players and raises an exception if so."""
        if (
            Stat.objects.filter(team=self.team).count() >= 5
            and not Stat.objects.filter(player=self.player, team=self.team).exists()
        ):
            raise ValidationError(f"The team '{self.team.uuid}' already has 5 players.")

    def clean(self, *args, **kwargs):
        self.clean_players()
        return super().clean()

    def __str__(self):
        return self.player.username
