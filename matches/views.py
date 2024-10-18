from django.views import View
from django.db.models import F, Subquery, OuterRef, Case, When, Value
from players.models import Player
from stats.models import Stat
from matches.models import Match
from django.shortcuts import render

class MatchHistory(View):

    def get(self, request):
        mvp_subquery = Stat.objects.filter(team__match=OuterRef("pk"), mvp=True).values(
            "player__username"
        )[:1]


        matches = Match.objects.select_related("map", "winner").prefetch_related(
            "teams__stats__player", "teams__players__main_agent"
        )

        matches = matches.annotate(
            mvp=Subquery(mvp_subquery),
            mvp_icon=Subquery(
                Player.objects.filter(username=OuterRef("mvp"))
                .values("main_agent__icon")[:1]
            )
        )

        return render(request, "matches/match_history.html", {"matches": matches})
