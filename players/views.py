from allauth.account.views import SignupView, LoginView, LogoutView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from players.forms import PlayerLoginForm, PlayerSignupForm
from players.models import Player


class PlayerLoginView(LoginView):
    form_class = PlayerLoginForm
    template_name = "players/account_forms.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form_title"] = "Login"
        ctx["form_action"] = reverse_lazy("account_login")
        return ctx


class PlayerRegistrationView(SignupView):
    template_name = "players/account_forms.html"
    form_class = PlayerSignupForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form_title"] = "Sign Up"
        ctx["form_action"] = reverse_lazy("account_signup")
        return ctx


class PlayerLogoutView(LogoutView):
    next_page = "home"


class PlayerProfileView(UpdateView):
    model = Player
    template_name = "players/player_profile.html"
    context_object_name = "player"
    success_url = reverse_lazy("player_profile")
    fields = [
        "email",
        "username",
        "main_agent",
        "tier",
    ]

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        queryset = Player.objects.filter(username=username)
        if not queryset.exists():
            raise Http404("Player does not exist")
        queryset = Player.annotate_wins_and_losses(queryset)
        queryset = Player.annotate_mvp_and_ace(queryset)
        queryset = Player.annotate_kills_deaths_assists(queryset)
        queryset = Player.annotate_kda(queryset)
        queryset = Player.annotate_win_rate(queryset)
        queryset = Player.annotate_points(queryset)
        queryset = Player.annotate_kda(queryset)
        return queryset[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_edit"] = self.request.user.username == self.kwargs.get("username")
        return context
