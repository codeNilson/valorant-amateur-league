from rest_framework import serializers
from .models import Match


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = [
            "uuid",
            "url",
            "winner",
            "map",
            "youtube_url",
            "created_at",
        ]
        read_only_fields = [
            "uuid",
            "created_at",
        ]
        extra_kwargs = {
            "url": {
                "view_name": "matches:match-detail",
                "lookup_field": "uuid",
            },
        }
