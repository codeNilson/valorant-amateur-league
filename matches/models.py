import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Match(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    map = models.ForeignKey(
        "gamedata.Map", on_delete=models.SET_NULL, related_name="matches", null=True
    )
    winner = models.ForeignKey(
        "teams.Team",
        on_delete=models.SET_NULL,
        related_name="matches",
        null=True,
        blank=True,
    )
    youtube_url = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at.strftime("%d/%m/%Y")} - {self.map}"

    class Meta:
        verbose_name_plural = _("Matches")
