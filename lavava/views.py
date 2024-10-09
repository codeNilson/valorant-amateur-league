from django.db.models import When, Case, F
from django.db import models
from django.shortcuts import redirect
from django.views.generic import TemplateView
from players.models import Player
from utils import calc_kda, calc_win_ratio


class LandingPageView(TemplateView):
    template_name = "lavava/landing_page.html"


class HomeView(TemplateView):
    template_name = "lavava/home.html"

    def get_players_ranking(self):
        players = Player.objects.select_related("main_agent", "rankinglog")
        players = Player.annotate_wins_and_losses(players)
        players = Player.annotate_mvp_and_ace(players)
        players = Player.annotate_kills_deaths_assists(players)
        players = Player.annotate_points(players)
        players = Player.annotate_kda(players)
        players = players.annotate(
            winratio=F("wins") / (F("wins") + F("losses"))
        )

        for player in players:

            # player.winratio = calc_win_ratio(
            #     wins=player.wins,
            #     losses=player.losses,
            # )
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
