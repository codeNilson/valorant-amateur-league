from django.contrib import admin
from .models import Stat


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = [
        "player",
        "team",
        "agent",
        "kills",
        "deaths",
        "assists",
        "mvp",
        "ace",
    ]

    search_fields = [
        "player__username",
        "team__uuid",
        "agent__name",
    ]

    list_filter = [
        "agent",
    ]
