from django.db.models import Count, F, Q, Sum
from django.shortcuts import redirect
from django.views.generic import TemplateView
from players.models import Player
from utils import calc_kda, calc_win_ratio


class LandingPageView(TemplateView):
    template_name = "lavava/landing_page.html"


class HomeView(TemplateView):
    template_name = "lavava/home.html"

    def get_players_ranking(self):
        players = (
            Player.objects.select_related("main_agent", "rankinglog")
            .annotate(
                wins=Count(
                    "teams", filter=Q(teams__matches__winner__id=F("teams__id"))
                ),
                losses=Count(
                    "teams", filter=~Q(teams__matches__winner__id=F("teams__id"))
                ),
                mvp=Count("stats", filter=Q(stats__mvp=True)),
                ace=Count("stats", filter=Q(stats__ace=True)),
            )
            .annotate(
                total_kills=Sum("stats__kills"),
                total_deaths=Sum("stats__deaths"),
                total_assists=Sum("stats__assists"),
                points=F("mvp") + F("ace") + F("wins") * 3,
            )
        )

        for player in players:

            player.winratio = calc_win_ratio(
                wins=player.wins,
                losses=player.losses,
            )
            player.kda = calc_kda(
                kills=player.total_kills,
                assists=player.total_assists,
                deaths=player.total_deaths,
            )
            player.position_changes = player.rankinglog.get_position_class()

        players = sorted(players, key=lambda p: (p.points, p.mvp, p.ace), reverse=True)

        return players

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        players = self.get_players_ranking()
        ctx["players"] = players
        ctx["update_at"] = players[0].rankinglog.updated_at.strftime("%d/%m/%Y")
        return ctx

    def post(self, request, *args, **kwargs):  # pylint: disable=unused-argument

        players = self.get_players_ranking()

        for index, player in enumerate(players, start=1):
            player.rankinglog.save_position_changes(index)

        return redirect("home")
