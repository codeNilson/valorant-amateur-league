from rest_framework import serializers
from gamedata.models import Tier


class TierSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tiers-detail")

    class Meta:
        model = Tier
        fields = [
            "url",
            "tier",
            "division",
            "small_icon",
            "large_icon",
        ]
