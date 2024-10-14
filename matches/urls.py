from . import views
from django.urls import path


app_name = "matches"

urlpatterns = [
    path("history/", views.MatchHistory.as_view(), name="history"),
]
