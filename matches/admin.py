from django.contrib import admin
from .models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = [
        "uuid",
        "map",
        "winner",
        "created_at",
    ]

    list_display_links = [
        "uuid",
        "winner",
    ]

    list_editable = [
        "map",
    ]

    search_fields = [
        "uuid",
    ]

    list_filter = [
        "created_at",
        "map",
    ]

    ordering = [
        "-created_at",
    ]
