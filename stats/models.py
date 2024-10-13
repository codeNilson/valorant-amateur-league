from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


# pylint: disable=unused-variable,unused-argument
class Stat(models.Model):
    player = models.ForeignKey(
        "players.Player", on_delete=models.CASCADE, related_name="stats"
    )
    team = models.ForeignKey(
        "teams.Team",
        on_delete=models.CASCADE,
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
        if self.kills is not None and self.assists is not None:

            if not self.deaths:
                return round((self.kills + self.assists), 2)

            return round((self.kills + self.assists) / self.deaths, 2)
        return None

    def clean_players(self):
        """Checks if the team already has five players stats and raises an exception if so."""
        team_has_five_players = Stat.objects.filter(team=self.team).count() >= 5
        player_not_in_team = not Stat.objects.filter(
            player=self.player, team=self.team
        ).exists()

        if team_has_five_players and player_not_in_team:
            raise ValidationError(
                _("The team '%(team)s' already has 5 players.")
                % {"team": self.team.uuid},
                code="team_full",
            )

    def clean(self, *args, **kwargs):
        self.clean_players()
        return super().clean()

    def __str__(self):
        return self.player.username
