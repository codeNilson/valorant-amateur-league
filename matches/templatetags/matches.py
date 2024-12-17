from django import template
from django.core.cache import cache
from django.db.models import OuterRef, Subquery
from django.template.defaultfilters import stringfilter
from matches.models import Match
from stats.models import Stat

register = template.Library()


@register.inclusion_tag("global/partials/list_matches.html", takes_context=True)
def match_history(context):
    if cache.get("matches"):
        print("Cache hit")
        matches = cache.get("matches")
    else:
        print("Cache miss")
        mvp_subquery = Stat.objects.filter(team__match=OuterRef("pk"), mvp=True).values(
            "player__username"
        )[:1]
        mvp_icon_subquery = Stat.objects.filter(
            team__match=OuterRef("pk"), mvp=True
        ).values("agent__icon")[:1]

        matches = (
            Match.objects.filter(is_finished=True)
            .select_related("map", "winner")
            .prefetch_related("teams__stats__player", "teams__players__main_agent")
        )

        matches = matches.annotate(
            mvp=Subquery(mvp_subquery),
            mvp_icon=Subquery(mvp_icon_subquery),
        )

        cache.set("matches", matches, timeout=60 * 30)

    # if username is provided in the url, filter matches where the player is the mvp
    username = context["request"].resolver_match.kwargs.get("username")
    if username:
        matches = matches.filter(teams__stats__player__username=username)

    return {"matches": matches}


@register.filter(is_safe=True)
@stringfilter
def get_embed_url(youtube_url):
    return youtube_url.replace("watch?v=", "embed/")
