from rest_framework import serializers
from teams.models import Team
from matches.models import Match
from players.models import Player


class TeamSerializer(serializers.ModelSerializer):

    players = serializers.SerializerMethodField()
    players_uuid = serializers.ListField(
        child=serializers.UUIDField(), write_only=True, required=False
    )
    match = serializers.StringRelatedField(read_only=True)
    match_uuid = serializers.UUIDField(write_only=True, required=False)

    def get_players(self, obj):
        return [
            {
                "uuid": player.uuid,
                "username": player.username,
            }
            for player in obj.players.all()
        ]

    def create(self, validated_data):
        try:
            uuid = validated_data.pop("match_uuid", None)
            if uuid:
                match = Match.objects.get(uuid=uuid)
                validated_data["match"] = match

        except Match.DoesNotExist as exc:
            raise serializers.ValidationError(
                {"match": "Didn't find a match with the provided UUID."}
            ) from exc

        players_uuids = validated_data.pop("players_uuid", [])
        players = []
        for uuid in players_uuids:
            try:
                player = Player.objects.get(uuid=uuid)
                players.append(player)
            except Player.DoesNotExist as exc:
                raise serializers.ValidationError(
                    {
                        "players": "Didn't find a player with the UUID %(uuid)s."
                        % {"uuid": uuid}
                    }
                ) from exc

        validated_data["players"] = players

        return super().create(validated_data)

    class Meta:

        model = Team

        fields = [
            "url",
            "uuid",
            "match",
            "match_uuid",
            "players",
            "players_uuid",
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
