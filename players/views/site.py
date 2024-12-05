from allauth.account.views import SignupView, LoginView, LogoutView
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from players.forms import PlayerLoginForm, PlayerSignupForm, PlayerModelForm


class PlayerLoginView(LoginView):
    form_class = PlayerLoginForm
    template_name = "players/account_forms.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "form_title": "Login",
                "form_action": reverse_lazy("account_login"),
                "submit_text": "Login",
            }
        )
        return ctx


class PlayerRegistrationView(SignupView):
    template_name = "players/account_forms.html"
    form_class = PlayerSignupForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "form_title": _("Sign Up"),
                "form_action": reverse_lazy("signup"),
                "submit_text": _("Sign Up"),
            }
        )
        return ctx


class PlayerLogoutView(LogoutView):
    next_page = "home"


class PlayerProfileView(SuccessMessageMixin, UpdateView):
    form_class = PlayerModelForm
    template_name = "players/player_profile.html"
    context_object_name = "player"
    success_message = _("Profile updated successfully!")

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        player_model = get_user_model()
        queryset = player_model.objects.filter(username=username).select_related(
            "main_agent", "tier"
        )
        if not queryset.exists():
            raise Http404(_("Player does not exist"))
        queryset = player_model.annotate_wins_and_losses(queryset)
        queryset = player_model.annotate_mvp_and_ace(queryset)
        queryset = player_model.annotate_kills_deaths_assists(queryset)
        queryset = player_model.annotate_kda(queryset)
        queryset = player_model.annotate_win_rate(queryset)
        queryset = player_model.annotate_points(queryset)
        queryset = player_model.annotate_kda(queryset)
        return queryset.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_label = _("I want to be included in the draft")
        context.update(
            {
                "can_edit": self.request.user.username == self.kwargs.get("username"),
                "submit_text": _("Save"),
                "draft_label": draft_label,
            }
        )
        return context
