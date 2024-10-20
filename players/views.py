from allauth.account.views import SignupView, LoginView, LogoutView
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
        return get_object_or_404(Player, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_edit"] = self.request.user.username == self.kwargs.get("username")
        return context
