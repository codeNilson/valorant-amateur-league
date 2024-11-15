from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):

    tier = serializers.StringRelatedField()
    main_agent = serializers.SerializerMethodField()
    ranking = serializers.SerializerMethodField()
    social_accounts = serializers.SerializerMethodField()

    def get_main_agent(self, obj):
        return {
            "uuid": obj.main_agent.uuid,
            "name": obj.main_agent.name,
        }

    def get_ranking(self, obj):
        return obj.rankinglog.last_position

    def get_social_accounts(self, obj):
        return [
            {"provider": account.provider, "uid": account.uid}
            for account in obj.socialaccount_set.all()
            if account.provider == "discord"
        ]

    class Meta:
        model = Player
        fields = [
            "url",
            "uuid",
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
