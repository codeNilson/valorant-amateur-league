import uuid
from django.db import models
from django.forms import ValidationError


class Team(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    players = models.ManyToManyField(
        "players.Player",
        through="stats.Stat",
        related_name="teams",
    )
    match = models.ForeignKey(
        "matches.Match",
        on_delete=models.SET_NULL,
        related_name="teams",
        null=True,
        blank=True,
    )

    def get_players(self):
        return self.players.all()

    def get_players_perfomance(self):
        return self.stats.all()

    def clean_match(self):
        """Check if the match has already two teams."""
        if (
            self.match is not None
            and self.match.teams.count() >= 2
            and not self.match.teams.filter(uuid=self.uuid).exists()
        ):
            raise ValidationError("A match can only have two teams.")

    def clean(self) -> None:
        self.clean_match()
        return super().clean()

    def __str__(self):
        return str(self.uuid)
