from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", views.LandingPageView.as_view(), name="landing_page"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("matches/", include("matches.urls")),
    # django-allauth urls
    path("accounts/", include("players.urls")),
    path("accounts/", include("allauth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
