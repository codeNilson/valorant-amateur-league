from django.contrib import admin
from .models import Team
from stats.models import Stat


class PlayerInline(admin.StackedInline):
    model = Team.players.through
    extra = 1
    fields = [
        "player",
    ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "uuid",
        "match",
    ]

    search_fields = [
        "players",
        "match",
    ]

    list_filter = [
        "players",
        "match",
    ]

    inlines = [
        PlayerInline,
    ]
