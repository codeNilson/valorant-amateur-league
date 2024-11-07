from rest_framework import viewsets
from players.models import Player
from players.serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    http_method_names = ["get"]
    lookup_field = "uuid"
    # lookup_url_kwarg = "uuid"
    # filter_backends = [filters.SearchFilter]
    # search_fields = [
    #     "name",
    #     "email",
    #     "phone",
    #     "address",
    #     "city",
    #     "state",
    #     "country",
    #     "zip_code",
    # ]
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_staff=False)
