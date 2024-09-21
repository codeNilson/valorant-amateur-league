from django.db import models
from django.contrib.auth.models import AbstractUser
from gamedata.models import Tier


class Player(AbstractUser):
    # matches = models.ManyToManyField(Match, through="Stat", related_name="players")
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, related_name="players", null=True)
