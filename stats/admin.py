from django.contrib import admin
from .models import Stat


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "player",
                    "team",
                ],
            },
        ),
        (
            "Player Stats",
            {
                "fields": [
                    "agent",
                    "kills",
                    "deaths",
                    "assists",
                    "mvp",
                    "ace",
                ],
            },
        ),
    ]

    readonly_fields = [
        "player",
        "team",
    ]

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
        "player",
    ]

    list_select_related = [
        "player",
        "team",
        "agent",
    ]

    list_per_page = 10
