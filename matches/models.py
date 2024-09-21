from django.db import models


class Match(models.Model):
    uuid = models.UUIDField()
    map = models.ForeignKey(
        "gamedata.Map", on_delete=models.CASCADE, related_name="matches", null=True
    )
    winner = models.ForeignKey(
        "teams.Team", on_delete=models.CASCADE, related_name="matches", null=True
    )

    def __str__(self):
        return self.map
