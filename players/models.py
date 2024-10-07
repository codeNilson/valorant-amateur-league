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
