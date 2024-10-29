from allauth.account.views import SignupView, LoginView, LogoutView
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from players.forms import PlayerLoginForm, PlayerSignupForm, PlayerModelForm


class PlayerLoginView(LoginView):
    form_class = PlayerLoginForm
    template_name = "players/account_forms.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "form_title": "Login",
            "form_action": reverse_lazy("account_login"),
            "submit_text":"Login",
}) 
        return ctx


class PlayerRegistrationView(SignupView):
    template_name = "players/account_forms.html"
    form_class = PlayerSignupForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form_title"] = "Sign Up"
        ctx["form_action"] = reverse_lazy("account_signup")
        ctx["submit_text"] = "Sign Up"
        return ctx


class PlayerLogoutView(LogoutView):
    next_page = "home"


class PlayerProfileView(SuccessMessageMixin, UpdateView):
    form_class = PlayerModelForm
    template_name = "players/player_profile.html"
    context_object_name = "player"
    success_message = "Profile updated successfully!"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        player_model = get_user_model()
        queryset = player_model.objects.filter(username=username)
        if not queryset.exists():
            raise Http404("Player does not exist")
        queryset = player_model.annotate_wins_and_losses(queryset)
        queryset = player_model.annotate_mvp_and_ace(queryset)
        queryset = player_model.annotate_kills_deaths_assists(queryset)
        queryset = player_model.annotate_kda(queryset)
        queryset = player_model.annotate_win_rate(queryset)
        queryset = player_model.annotate_points(queryset)
        queryset = player_model.annotate_kda(queryset)
        return queryset[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_edit"] = self.request.user.username == self.kwargs.get("username")
        context["submit_text"] = "Save"
        return context
