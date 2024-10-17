from django.db.models import Subquery, OuterRef
from stats.models import Stat
from matches.models import Match
from django.shortcuts import render
from django.views import View


# Create your views here.
class MatchHistory(View):

    def get(self, request):
        # Subconsulta para obter o jogador MVP para cada partida
        mvp_subquery = Stat.objects.filter(
            team__match=OuterRef("pk"), mvp=True
        ).values("player__username")[:1]

        matches = Match.objects.prefetch_related("map", "winner", "teams__stats__player", "teams__players__main_agent")
        matches = matches.annotate(mvp=Subquery(mvp_subquery))

        return render(request, "matches/match_history.html", {"matches": matches})
