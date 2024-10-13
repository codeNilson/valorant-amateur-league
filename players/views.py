from allauth.account.views import LoginView, LogoutView, SignupView
from django.urls import reverse_lazy
from players.forms import PlayerLoginForm, PlayerSignupForm


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
