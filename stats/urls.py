from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"api/v1", views.StatViewSet)

app_name = "stats"

urlpatterns = [
    path("", include(router.urls)),
]
