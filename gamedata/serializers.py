from rest_framework import serializers
from gamedata.models import Map


class MapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Map
        fields = [
            "uuid",
            "name",
            "splash",
        ]
