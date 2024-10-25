from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model


class LandingPageView(TemplateView):
    template_name = "lavava/landing_page.html"


class HomeView(TemplateView):
    template_name = "lavava/home.html"

    def get_players_ranking(self):
        player_model = get_user_model()
        players = player_model.objects.select_related("main_agent", "rankinglog")
        players = player_model.annotate_wins_and_losses(players)
        players = player_model.annotate_mvp_and_ace(players)
        players = player_model.annotate_kills_deaths_assists(players)
        players = player_model.annotate_points(players)
        players = player_model.annotate_kda(players)
        players = player_model.annotate_win_rate(players)

        for player in players:
            player.position_changes = player.rankinglog.get_position_class()

        players = sorted(players, key=lambda p: (p.points, p.mvp, p.ace), reverse=True)

        return players

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        players = self.get_players_ranking()
        ctx["players"] = players
        ctx["update_at"] = players[0].rankinglog.updated_at  #  solução não ideal
        return ctx

    def post(self, request, *args, **kwargs):  # pylint: disable=unused-argument

        players = self.get_players_ranking()

        for index, player in enumerate(players, start=1):
            player.rankinglog.save_position_changes(index)

        return redirect("home")
