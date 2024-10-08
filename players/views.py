from django.contrib.auth.views import LogoutView


class PlayerLogoutView(LogoutView):
    next_page = "home"
