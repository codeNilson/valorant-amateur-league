from rest_framework.routers import DefaultRouter
from gamedata import views


router = DefaultRouter()
router.register(r"api/v1", views.MapViewSet, basename="map")


urlpatterns = router.urls
