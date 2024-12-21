from django.urls import include, path
from rest_framework.routers import DefaultRouter
from players import views

router = DefaultRouter()
router.register(r"api/v1", views.PlayerViewSet, basename="player")
router.register(
    r"api/v1/by-uid", views.PlayerByDiscordUidViewSet, basename="player-by-uid"
)

urlpatterns = [
    path("login/", views.PlayerLoginView.as_view(), name="login"),
    path("signup/", views.PlayerRegistrationView.as_view(), name="signup"),
    path("logout/", views.PlayerLogoutView.as_view(), name="logout"),
    path(
        "profile/<str:username>",
        views.PlayerProfileView.as_view(),
        name="account_profile",
    ),
    # API
    path("", include(router.urls)),
]
