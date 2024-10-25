from django import template
from django.db.models import OuterRef, Subquery
from django.template.defaultfilters import stringfilter
from django.contrib.auth import get_user_model
from matches.models import Match
from stats.models import Stat

register = template.Library()


@register.inclusion_tag("global/partials/list_matches.html", takes_context=True)
def match_history(context, username=None):
    mvp_subquery = Stat.objects.filter(team__match=OuterRef("pk"), mvp=True).values(
        "player__username"
    )[:1]

    matches = Match.objects.select_related("map", "winner").prefetch_related(
        "teams__stats__player", "teams__players__main_agent"
    )

    player_model = get_user_model()
    matches = matches.annotate(
        mvp=Subquery(mvp_subquery),
        mvp_icon=Subquery(
            player_model.objects.filter(username=OuterRef("mvp")).values(
                "main_agent__icon"
            )[:1]
        ),
    )

    # if username is provided in the url, filter matches where the player is the mvp
    username = context["request"].resolver_match.kwargs.get("username")
    if username:
        matches = matches.filter(mvp=username)

    return {"matches": matches}


@register.filter(is_safe=True)
@stringfilter
def get_embed_url(youtube_url):
    return youtube_url.replace("watch?v=", "embed/")
