import uuid
from datetime import datetime
from django.db import models
from django.db.models.functions import Cast
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Round


class Player(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tier = models.ForeignKey(
        "gamedata.Tier",
        on_delete=models.SET_NULL,
        related_name="players",
        blank=True,
        null=True,
    )
    main_agent = models.ForeignKey(
        "gamedata.Agent",
        on_delete=models.SET_NULL,
        null=True,
    )

    @staticmethod
    def annotate_wins_and_losses(queryset):
        return queryset.annotate(
            wins=models.Count(
                "teams",
                filter=models.Q(teams__matches__winner__id=models.F("teams__id")),
            ),
            losses=models.Count(
                "teams",
                filter=~models.Q(teams__matches__winner__id=models.F("teams__id")),
            ),
        )

    @staticmethod
    def annotate_mvp_and_ace(queryset):
        return queryset.annotate(
            mvp=models.Count("stats", filter=models.Q(stats__mvp=True)),
            ace=models.Count("stats", filter=models.Q(stats__ace=True)),
        )

    @staticmethod
    def annotate_kills_deaths_assists(queryset):
        return queryset.annotate(
            total_kills=models.Sum("stats__kills"),
            total_deaths=models.Sum("stats__deaths"),
            total_assists=models.Sum("stats__assists"),
        )

    @staticmethod
    def annotate_points(queryset):
        return queryset.annotate(
            points=models.F("mvp") + models.F("ace") + models.F("wins") * 3
        )

    @staticmethod
    def annotate_kda(queryset):
        return queryset.annotate(
            kda=models.Case(
                models.When(
                    total_deaths=0,
                    then=models.F("total_kills") + models.F("total_assists"),
                ),
                default=Round(
                    (
                        Cast(models.F("total_kills"), models.FloatField())
                        + Cast(models.F("total_assists"), models.FloatField())
                    )
                    / Cast(models.F("total_deaths"), models.FloatField()),
                    2,
                ),
                output_field=models.FloatField(),
            )
        )

    @staticmethod
    def annotate_win_ratio(queryset):
        return queryset.annotate(
            win_ratio=models.Case(
                models.When(models.Q(wins=0) & models.Q(losses=0), then=0),
                default=Cast(models.F("wins"), models.FloatField())
                / (
                    Cast(models.F("wins"), models.FloatField())
                    + Cast(models.F("losses"), models.FloatField())
                ),
                output_field=models.FloatField(),
            )
            * 100
        )


class RankingLog(models.Model):
    player = models.OneToOneField("players.Player", on_delete=models.CASCADE)
    last_position = models.IntegerField(
        default=0, help_text="Last position in the ranking"
    )
    last_position_change = models.IntegerField(
        default=0,
        help_text="Show if the player went up or down in the ranking since the last update",
    )
    updated_at = models.DateTimeField(auto_now=True)

    def get_position_class(self) -> str:
        if self.last_position_change < 0:
            return "fa-caret-down"
        if self.last_position_change > 0:
            return "fa-caret-up"
        return "fa-minus"

    def save_position_changes(self, index: int) -> None:
        self.last_position_change = (index - self.last_position) * (-1)
        self.last_position = index
        self.updated_at = datetime.today().date()
        self.full_clean()
        self.save()
