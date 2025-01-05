from rest_framework import viewsets
from players.models import Player
from players.serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    http_method_names = ["get"]
    lookup_field = "username"

    def get_queryset(self):
        queryset = Player.objects.select_related(
            "main_agent",
            "tier",
            "rankinglog",
        ).prefetch_related("socialaccount_set")
        return queryset


class PlayerByDiscordUidViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    http_method_names = ["get"]
    lookup_field = "socialaccount__uid"

    def get_queryset(self):
        queryset = Player.objects.select_related(
            "main_agent",
            "tier",
            "rankinglog",
        ).prefetch_related("socialaccount_set")
        return queryset
