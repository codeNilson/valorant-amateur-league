from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from teams.serializers import TeamSerializer
from teams.models import Team


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all().select_related("match").prefetch_related("players")

    serializer_class = TeamSerializer
    lookup_field = "uuid"
