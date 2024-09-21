from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "tier",
        "email",
    ]

    list_editable = [
        "tier",
    ]

    list_filter = [
        "tier",
    ]

    search_fields = [
        "username",
        "first_name",
        "email",
    ]
