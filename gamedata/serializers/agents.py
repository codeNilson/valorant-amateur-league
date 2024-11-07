from rest_framework import serializers
from gamedata.models import Agent


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = [
            "uuid",
            "url",
            "name",
            "icon",
            "small_icon",
        ]
        extra_kwargs = {
            "url": {
                "view_name": "agents-detail",
                "lookup_field": "uuid",
            },
        }
