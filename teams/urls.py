from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teams.views.api import TeamViewSet

router = DefaultRouter()
router.register(r"api/v1", TeamViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
