from allauth.account.views import LoginView, LogoutView, SignupView
from players.forms import PlayerLoginForm


class PlayerLoginView(LoginView):
    form_class = PlayerLoginForm
    template_name = "players/login.html"


class PlayerRegistrationView(SignupView):
    pass


class PlayerLogoutView(LogoutView):
    next_page = "home"
