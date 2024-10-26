from django.urls import path
from . import views

app_name = "shared"

urlpatterns = [
    path("maps", views.MapsView.as_view(), name="maps"),
    path("agents", views.AgentsView.as_view(), name="agents"),
]
