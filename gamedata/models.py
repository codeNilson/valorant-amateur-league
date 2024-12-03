import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models


class Agent(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20, unique=True, verbose_name=_("Agent Name"))
    description = models.TextField(verbose_name=_("Description"))
    role = models.ForeignKey(
        "Role",
        on_delete=models.SET_NULL,
        related_name="agents",
        blank=True,
        null=True,
        verbose_name=_("Role"),
    )
    icon = models.CharField(max_length=255, verbose_name=_("Icon"))
    small_icon = models.CharField(max_length=255, verbose_name=_("Small Icon"))
    full_portrait = models.CharField(max_length=255, verbose_name=_("Full Portrait"))
    background = models.CharField(max_length=255, verbose_name=_("Background"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Agent")
        verbose_name_plural = _("Agents")


class Role(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=20, unique=True, verbose_name=_("Role Name"))
    description = models.TextField(verbose_name=_("Description"))
    icon = models.CharField(max_length=255, verbose_name=_("Icon"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")

class Map(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=20, unique=True, verbose_name=_("Map Name"))
    splash = models.CharField(max_length=255, verbose_name=_("Splash Art"))
    vertical_icon = models.CharField(max_length=255, verbose_name=_("Vertical Icon"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Map")
        verbose_name_plural = _("Maps")


class Tier(models.Model):
    tier = models.CharField(max_length=20, unique=True, verbose_name=_("Tier"))
    division = models.CharField(max_length=20, verbose_name=_("Division"))
    small_icon = models.CharField(max_length=255, verbose_name=_("Small Icon"))
    large_icon = models.CharField(max_length=255, verbose_name=_("Large Icon"))

    def __str__(self):
        return self.tier

    class Meta:
        verbose_name = _("Tier")
        verbose_name_plural = _("Tiers")
