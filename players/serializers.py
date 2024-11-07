from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "uuid",
            "username",
            "email",
            "main_agent",
            "tier",
            "url",
        ]
        extra_kwargs = {"url": {"view_name": "player-detail", "lookup_field": "uuid"}}
