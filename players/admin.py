from django.contrib import admin
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission
from .models import Player, RankingLog


# @admin.register(Player)
# class PlayerAdmin(admin.ModelAdmin):
#     pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Player Info",
            {
                "fields": (
                    "uuid",
                    "username",
                    "password",
                    "email",
                    "tier",
                    "main_agent",
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
                    "is_approved",
                    "include_in_draft",
                    "will_play_the_next_match",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
                "description": _("Permissions can be changed in the User Permissions section."),
            },
        ),
    )

    list_display = [
        "username",
        "tier",
        "main_agent",
        "email",
        "is_approved",
        "include_in_draft",
        "will_play_the_next_match",
    ]

    list_editable = [
        "include_in_draft",
        "is_approved",
        "will_play_the_next_match",
    ]

    readonly_fields = [
        "last_login",
        "uuid",
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

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "user_permissions":
            kwargs["queryset"] = Permission.objects.all().select_related("content_type")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        # If the password is changed, update it
        if "password" in form.changed_data:
            obj.set_password(form.cleaned_data["password"])
        if "is_approved" in form.changed_data and obj.is_approved:
            send_mail(
                "Sua conta foi ativada!",
                "Parabéns! Sua conta foi ativada e você já pode acessar o sistema.",
                None,
                [obj.email],
                fail_silently=False,
            )
            print(f"Email sent to {obj.email}")
        super().save_model(request, obj, form, change)


@admin.register(RankingLog)
class RankingLogAdmin(admin.ModelAdmin):

    readonly_fields = [
        "last_position",
        "last_position_change",
    ]

    list_display = [
        "player",
        "last_position",
        "last_position_change",
        "updated_at",
    ]

    search_fields = [
        "player__username",
    ]

    list_per_page = 10
