from django.contrib import admin
from .models import Agent, Role, Map, Tier


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {"fields": ("name", "role")}),
        (
            "Image URLs",
            {
                "fields": (
                    "icon",
                    "small_icon",
                    "full_portrait",
                    "background",
                )
            },
        ),
        ("Description", {"fields": ("description",)}),
    )

    list_display = [
        "name",
        "role",
    ]

    list_filter = [
        "role",
    ]

    list_editable = [
        "role",
    ]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    fields = [
        "name",
        "uuid",
        "description",
        "icon",
    ]

    readonly_fields = [
        "uuid",
    ]


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name", "uuid")}),
        (
            "Image URLs",
            {
                "fields": (
                    "display_icon",
                    "list_horizontal_icon",
                    "list_vertical_icon",
                    "splash",
                )
            },
        ),
    )

    list_display = [
        "name",
        "uuid",
    ]

    readonly_fields = [
        "uuid",
    ]


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {"fields": ("tier", "division")}),
        (
            "Image URLs",
            {
                "fields": (
                    "small_icon",
                    "large_icon",
                )
            },
        ),
    )

    list_display = [
        "tier",
        "division",
    ]

    list_filter = [
        "division",
    ]
