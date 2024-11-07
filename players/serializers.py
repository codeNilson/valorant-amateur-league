from rest_framework import serializers
from gamedata import serializers as gamedata_serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):

    main_agent = gamedata_serializers.AgentSerializer()
    tier = gamedata_serializers.TierSerializer()

    class Meta:
        model = Player
        fields = [
            "uuid",
            "url",
            "username",
            "email",
            "main_agent",
            "tier",
        ]
        extra_kwargs = {
            "url": {
                "view_name": "player-detail",
                "lookup_field": "uuid",
            },
        }
