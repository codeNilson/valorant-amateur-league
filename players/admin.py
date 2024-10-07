from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Player Info",
            {
                "fields": (
                    "username",
                    "password",
                    "first_name",
                    "email",
                    "tier",
                    "main_agent",
                    "last_position",
                    "last_login",
                    "date_joined",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
                "description": "Permissions can be changed in the User Permissions section.",
            },
        ),
    )

    list_display = [
        "username",
        "first_name",
        "tier",
        "main_agent",
        "email",
        "last_position",
    ]

    list_editable = [
        "first_name",
        "tier",
        "main_agent",
    ]

    readonly_fields = [
        "last_login",
    ]

    list_select_related = [
        "tier",
        "main_agent",
    ]

    list_prefetch_related = [
        "stats",
    ]

    list_filter = [
        "tier__division",
    ]

    search_fields = [
        "username",
        "first_name",
        "email",
    ]

    list_per_page = 10

    def save_model(self, request, obj, form, change):
        # If the password is changed, update it
        if form.cleaned_data.get("password"):
            obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)
