from rest_framework import viewsets
from players.models import Player
from players.serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().select_related("tier", "main_agent", "rankinglog")
    serializer_class = PlayerSerializer
    http_method_names = ["get"]
    lookup_field = "uuid"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_staff=False)
