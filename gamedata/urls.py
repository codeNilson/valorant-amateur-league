from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import models, views


router = DefaultRouter()
router.register(r"agents/api/v1", views.AgentsViewSet, basename="agents")
router.register(r"tiers/api/v1", views.TiersViewSet, basename="tiers")

urlpatterns = [
    path("", include(router.urls)),
]
