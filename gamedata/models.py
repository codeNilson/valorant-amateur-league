import uuid
from django.db import models


class Agent(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, related_name="agents", blank=True, null=True
    )
    icon = models.CharField(max_length=255)
    small_icon = models.CharField(max_length=255)
    full_portrait = models.CharField(max_length=255)
    background = models.CharField(max_length=255)

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
    display_icon = models.CharField(max_length=255)
    list_horizontal_icon = models.CharField(max_length=255)
    list_vertical_icon = models.CharField(max_length=255)
    splash = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tier(models.Model):
    tier = models.CharField(max_length=20, unique=True)
    division = models.CharField(max_length=20)
    small_icon = models.ImageField(upload_to="tiers/icons/", null=True, blank=True)
    large_icon = models.ImageField(upload_to="tiers/icons/", null=True, blank=True)

    def __str__(self):
        return self.tier
