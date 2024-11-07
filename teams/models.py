import uuid
from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    players = models.ManyToManyField(
        "players.Player",
        through="stats.Stat",
        related_name="teams",
    )
    match = models.ForeignKey(
        "matches.Match",
        on_delete=models.CASCADE,
        related_name="teams",
        null=True,
        blank=True,
    )

    def clean_match(self):
        """Check if the match has already two teams."""

        if (
            self.match is not None
            and self.match.teams.count() >= 2
            and not self.match.teams.filter(uuid=self.uuid).exists()
        ):
            raise ValidationError(
                _(
                    "You can not add this teams to match %(match)s. This match already has 5 players."
                    % {"match": self.match}
                ),
                code="too_many_teams",
            )

    def clean(self):
        self.clean_match()
        return super().clean()

    def __str__(self):
        return str(self.uuid)
