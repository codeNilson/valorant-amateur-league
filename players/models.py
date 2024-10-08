from datetime import datetime
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tier = models.ForeignKey(
        "gamedata.Tier",
        on_delete=models.SET_NULL,
        related_name="players",
        blank=True,
        null=True,
    )
    main_agent = models.ForeignKey(
        "gamedata.Agent",
        on_delete=models.SET_NULL,
        null=True,
    )


class RankingLog(models.Model):
    player = models.OneToOneField("players.Player", on_delete=models.CASCADE)
    last_position = models.IntegerField(
        default=0, help_text="Last position in the ranking"
    )
    last_position_change = models.IntegerField(
        default=0,
        help_text="Show if the player went up or down in the ranking since the last update",
    )
    updated_at = models.DateTimeField(auto_now=True)

    def get_position_class(self) -> str:
        if self.last_position_change < 0:
            return "fa-caret-down"
        if self.last_position_change > 0:
            return "fa-caret-up"
        return "fa-minus"

    def save_position_changes(self, index: int) -> None:
        self.last_position_change = (index - self.last_position) * (-1)
        self.last_position = index
        self.updated_at = datetime.now()
        self.save()
