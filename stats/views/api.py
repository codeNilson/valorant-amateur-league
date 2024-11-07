from rest_framework.viewsets import ModelViewSet
from stats.models import Stat
from stats.serializers import StatSerializer


class StatViewSet(ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
