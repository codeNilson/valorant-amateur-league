from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("home/", views.LandingPageView.as_view(), name="landing_page"),
    path("", views.HomeView.as_view(), name="home"),
    path("matches/", include("matches.urls")),
    path("teams/", include("teams.urls")),
    path("players/", include("players.urls")),
    path("maps/", include("gamedata.urls")),
    # django-allauth urls
    path("accounts/", include("allauth.urls")),
    # django-rest-framework jwt
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    #riot test
    path("riot.txt", views.RioTest.as_view(), name="riot"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
