from rest_framework.viewsets import ModelViewSet
from teams.serializers import TeamSerializer
from teams.models import Team


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "uuid"
