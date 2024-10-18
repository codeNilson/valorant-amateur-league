from django.contrib import admin
from django.utils.translation import gettext_lazy as _
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
        "team__match",
        "agent",
        "kills",
        "deaths",
        "assists",
        "get_kda",
        "mvp",
        "ace",
    ]

    list_editable = [
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
        "team__match",
    ]

    list_select_related = [
        "player",
        "team",
        "agent",
    ]

    list_per_page = 10

    @admin.display(description=_("KDA"))
    def get_kda(self, obj):
        return obj.get_kda()
