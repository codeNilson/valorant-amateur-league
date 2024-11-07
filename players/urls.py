from django.urls import include, path
from players import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/v1", views.PlayerViewSet, basename="player")
print(router.urls)

urlpatterns = [
    path("login/", views.PlayerLoginView.as_view(), name="account_login"),
    path("signup/", views.PlayerRegistrationView.as_view(), name="account_signup"),
    path("logout/", views.PlayerLogoutView.as_view(), name="account_logout"),
    path(
        "profile/<str:username>",
        views.PlayerProfileView.as_view(),
        name="account_profile",
    ),
    # API
    path("", include(router.urls)),
]
