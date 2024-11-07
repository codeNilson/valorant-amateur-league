from rest_framework.viewsets import ModelViewSet
from matches.models import Match
from matches.serializers import MatchSerializer


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    lookup_field = "uuid"
