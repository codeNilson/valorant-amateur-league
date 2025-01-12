import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Match(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    map = models.ForeignKey(
        "gamedata.Map",
        on_delete=models.SET_NULL,
        related_name="matches",
        null=True,
        blank=True,
        verbose_name=_("Map"),
    )
    winner = models.ForeignKey(
        "teams.Team",
        on_delete=models.SET_NULL,
        related_name="matches",
        null=True,
        blank=True,
        verbose_name=_("Winning Team"),
    )
    youtube_url = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("YouTube URL")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    is_finished = models.BooleanField(
        default=False,
        verbose_name=_("Is Finished"),
    )

    def __str__(self):
        return f"{self.created_at.strftime('%d/%m/%Y')} - {self.map}"

    def clean_winner(self):
        if self.winner and self.winner not in self.teams.all():
            raise ValidationError(
                {"winner": _("Winner must be one of the teams in the match")},
                code="invalid",
            )

    def clean(self):
        self.clean_winner()
        return super().clean()

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")
