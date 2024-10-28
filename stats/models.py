from collections import defaultdict
from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


# pylint: disable=unused-variable,unused-argument
class Stat(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors = defaultdict(list)

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
    first_bloods = models.PositiveIntegerField(null=True, blank=True)
    plants = models.PositiveIntegerField(null=True, blank=True)
    spikes_defused = models.PositiveIntegerField(null=True, blank=True)
    average_points = models.PositiveIntegerField(null=True, blank=True)
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
            self.errors["team"].append(_("The team already has five players."))

    def clean_mvp(self):
        # Check if the player is both ace and mvp and raise an exception if so.

        if self.ace and self.mvp:
            self.errors["mvp"].append(
                ValidationError(
                    _("A player can't be both ace and mvp."),
                    code="ace_mvp_conflict",
                )
            )
            self.errors["ace"].append(
                ValidationError(
                    _("A player can't be both ace and mvp."),
                    code="ace_mvp_conflict",
                )
            )

        # Check if the team already has an mvp and raise an exception if so.
        team_has_mvp = self.team.stats.filter(mvp=True).exists()
        if self.mvp and team_has_mvp and self.team.stats.get(mvp=True) != self:
            self.errors["mvp"].append(
                ValidationError(_("The team already has an mvp."), code="team_has_mvp")
            )

    def clean(self, *args, **kwargs):
        self.errors.clear()
        self.clean_players()
        self.clean_mvp()

        if self.errors:
            raise ValidationError(self.errors)

        return super().clean()

    def __str__(self):
        return self.player.username
