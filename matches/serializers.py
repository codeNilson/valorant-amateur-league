from rest_framework import serializers
from .models import Match


class MatchSerializer(serializers.ModelSerializer):

    map = serializers.SerializerMethodField()
    winner = serializers.SerializerMethodField()

    def get_map(self, obj):  # change str
        if not obj.map:
            return None
        return obj.map.name

    def get_winner(self, obj):
        if not obj.winner:
            return None
        return str(obj.winner)

    class Meta:
        model = Match
        fields = [
            "url",
            "uuid",
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
