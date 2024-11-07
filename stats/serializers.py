from rest_framework import serializers
from .models import Stat


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = [
            "url",
            "player",
            "team",
            "agent",
            "kills",
            "deaths",
            "assists",
            "first_bloods",
            "plants",
            "spikes_defused",
            "average_points",
            "mvp",
            "ace",
        ]
        read_only_fields = [
            "url",
        ]

        extra_kwargs = {
            "url": {
                "view_name": "stats:stat-detail",
            },
        }
