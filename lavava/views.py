from django.db.models import Count, F, Q
from django.views.generic import TemplateView
from players.models import Player


class LandingPage(TemplateView):
    template_name = "lavava/landing_page.html"


class Home(TemplateView):
    template_name = "lavava/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        players = (
            Player.objects.prefetch_related("stats")
            .select_related("tier", "main_agent")
            .annotate(
                wins=Count(
                    "teams", filter=Q(teams__matches__winner__id=F("teams__id"))
                ),
                losses=Count(
                    "teams", filter=~Q(teams__matches__winner__id=F("teams__id"))
                ),
                mvp=Count("stats", filter=Q(stats__mvp=True)),
                ace=Count("stats", filter=Q(stats__ace=True)),
            ).annotate(kda=(F("stats__kills") + F("stats__assists")) / F("stats__deaths"))
        )

        for player in players:
            player.points = (player.mvp + player.ace) + player.wins * 3
            total = player.wins + player.losses
            player.winratio = (player.wins / total) * 100 if total > 0 else 0
        players = sorted(players, key=lambda p: (p.points, p.mvp, p.ace), reverse=True)
        ctx["players"] = players
        return ctx
