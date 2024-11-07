from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"api/v1", views.MatchViewSet)

app_name = "matches"

urlpatterns = [
    path("history/", views.MatchHistory.as_view(), name="history"),
]

urlpatterns += router.urls
