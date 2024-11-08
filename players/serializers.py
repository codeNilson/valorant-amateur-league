from rest_framework import serializers
from gamedata import serializers as gamedata_serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):

    main_agent = gamedata_serializers.AgentSerializer()
    tier = gamedata_serializers.TierSerializer()
    ranking = serializers.SerializerMethodField()
    social_accounts = serializers.SerializerMethodField()

    def get_ranking(self, obj):
        return obj.rankinglog.last_position

    def get_social_accounts(self, obj):
        return obj.socialaccount_set.values_list(
            "provider",
            "uid",
        )

    class Meta:
        model = Player
        fields = [
            "uuid",
            "url",
            "username",
            "main_agent",
            "tier",
            "ranking",
            "social_accounts",
        ]
        extra_kwargs = {
            "url": {
                "view_name": "player-detail",
                "lookup_field": "uuid",
            },
        }
