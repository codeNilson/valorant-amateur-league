from rest_framework.viewsets import ModelViewSet
from gamedata import models
from gamedata.serializers import AgentSerializer, TierSerializer


class AgentsViewSet(ModelViewSet):
    queryset = models.Agent.objects.all()
    serializer_class = AgentSerializer
    lookup_field = "uuid"
    http_method_names = "get"


class TiersViewSet(ModelViewSet):
    queryset = models.Tier.objects.all()
    serializer_class = TierSerializer
    http_method_names = "get"
