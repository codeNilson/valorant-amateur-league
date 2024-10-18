from django.contrib import admin
from teams.models import Team
from .models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Restringe as escolhas de winner para apenas os times relacionados à match
        if db_field.name == "winner" and request.resolver_match.kwargs.get("object_id"):
            match_id = request.resolver_match.kwargs.get("object_id")
            kwargs["queryset"] = Team.objects.filter(match=match_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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

    list_select_related = [
        "map",
        "winner",
    ]
