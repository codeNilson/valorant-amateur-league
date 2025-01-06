from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.views import View
from django.http import FileResponse
from django.contrib import messages
from dotenv import load_dotenv
import requests
from utils.discord_utils import DiscordWebhook, DiscordWidget

load_dotenv()


class LandingPageView(TemplateView):
    template_name = "lavava/landing_page.html"


class HomeView(TemplateView):
    template_name = "lavava/home.html"

    def get_players_ranking(self):
        player_model = get_user_model()
        players = player_model.objects.select_related(
            "main_agent", "rankinglog"
        ).filter(is_approved=True)
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
        ctx["update_at"] = (
            players[0].rankinglog.updated_at if players else None
        )  #  solução não ideal

        widget = requests.get(
            "https://discord.com/api/guilds/1243610772064698398/widget.json", timeout=10
        ).json()

        discord_widget = DiscordWidget.create_from_json(widget)

        ctx["discord_widget"] = discord_widget

        return ctx

    def post(self, request, *args, **kwargs):  # pylint: disable=unused-argument

        players = self.get_players_ranking()

        if not players:
            messages.error(request, _("No players found to update ranking."))
            return redirect("home")

        try:
            webhook = DiscordWebhook()
            webhook.send_ranking_update(players)
        except AttributeError as e:
            messages.error(
                request,
                _("Error sending ranking update to Discord: %(error)s") % {"error": e},
            )

        for index, player in enumerate(players, start=1):
            player.rankinglog.save_position_changes(index)

        messages.success(request, _("Ranking updated successfully!"))

        return redirect("home")


class RioTest(View):
    def get(self, request):
        return FileResponse(open("riot.txt", "rb"), as_attachment=True, filename="riot.txt")
