from django.views.generic import TemplateView


class MatchHistory(TemplateView):
    template_name = "matches/match_history.html"
