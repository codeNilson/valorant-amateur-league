import uuid
from django.db import models


class Agent(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, related_name="agents", blank=True, null=True
    )
    icon = models.ImageField(upload_to="agents/icons/")
    small_icon = models.ImageField(upload_to="agents/small_icons/")
    full_portrait = models.ImageField(upload_to="agents/full_portraits/")
    background = models.ImageField(upload_to="agents/backgrounds/")

    def __str__(self):
        return self.name


class Role(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Map(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=20, unique=True)
    vertical_icon = models.ImageField(upload_to="maps/vertical_icons/")
    splash = models.ImageField(upload_to="maps/splashes/")

    def __str__(self):
        return self.name


class Tier(models.Model):
    tier = models.CharField(max_length=20, unique=True)
    division = models.CharField(max_length=20)
    small_icon = models.ImageField(upload_to="tiers/small_icons/")
    large_icon = models.ImageField(upload_to="tiers/large_icons/")

    def __str__(self):
        return self.tier
