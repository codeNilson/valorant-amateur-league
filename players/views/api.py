from rest_framework import viewsets
from players.models import Player
from players.serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    http_method_names = ["get"]
    lookup_field = "username"

    def get_queryset(self):
        queryset = Player.objects.filter(is_approved=True, is_active=True)
        queryset = queryset.select_related(
            "main_agent",
            "tier",
            "rankinglog",
        )
        queryset = queryset.prefetch_related("socialaccount_set")
        return queryset
