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
        "email",
    ]

    list_editable = [
        "tier",
    ]

    readonly_fields = [
        "last_login",
    ]

    list_select_related = [
        "tier",
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
        if form.cleaned_data["password"]:
            obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)
