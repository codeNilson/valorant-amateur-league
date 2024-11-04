from django.urls import path
from players import views

urlpatterns = [
    path("login/", views.PlayerLoginView.as_view(), name="account_login"),
    path("signup/", views.PlayerRegistrationView.as_view(), name="account_signup"),
    path("logout/", views.PlayerLogoutView.as_view(), name="account_logout"),
    path(
        "profile/<str:username>",
        views.PlayerProfileView.as_view(),
        name="account_profile",
    ),
    # api
    path(
        "api/v1/players/",
        views.PlayerViewSet.as_view({"get": "list"}),
        name="player_list_create_api",
    ),
]
