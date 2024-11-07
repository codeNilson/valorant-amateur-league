from rest_framework import serializers
from .models import Team
from players.serializers import PlayerSerializer


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team

        fields = [
            "uuid",
            "match",
            "url",
            "players",
        ]

        read_only_fields = [
            "uuid",
            "url",
        ]

        extra_kwargs = {
            "url": {
                "view_name": "team-detail",
                "lookup_field": "uuid",
            },
        }

    players = PlayerSerializer(
        many=True,
        read_only=True,
    )

    match = serializers.StringRelatedField()
