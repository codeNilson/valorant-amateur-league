from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"api/v1", views.MatchViewSet)

app_name = "matches"

CACHE_TIMEOUT = 60 * 10  # 10 minutes

urlpatterns = [
    path(
        "history/",
        cache_page(CACHE_TIMEOUT)(views.MatchHistory.as_view()),
        name="history",
    ),
]

urlpatterns += router.urls
