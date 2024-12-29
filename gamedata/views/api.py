from rest_framework import viewsets
from gamedata.serializers import MapSerializer
from gamedata.models import Map


class MapViewSet(viewsets.ModelViewSet):
    serializer_class = MapSerializer
    http_method_names = ["get"]
    lookup_field = "name"
    queryset = Map.objects.all()
