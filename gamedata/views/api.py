from rest_framework.viewsets import ReadOnlyModelViewSet
from gamedata import models
from gamedata.serializers import AgentSerializer, TierSerializer


class AgentsViewSet(ReadOnlyModelViewSet):
    queryset = models.Agent.objects.all()
    serializer_class = AgentSerializer
    lookup_field = "uuid"


class TiersViewSet(ReadOnlyModelViewSet):
    queryset = models.Tier.objects.all()
    serializer_class = TierSerializer
