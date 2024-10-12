from django.urls import path
from players import views

urlpatterns = [
    path("login/", views.PlayerLoginView.as_view(), name="account_login"),
    path("signup/", views.PlayerRegistrationView.as_view(), name="account_signup"),
    path("logout/", views.PlayerLogoutView.as_view(), name="account_logout"),
    # path('accounts/password/change/', allauth_views.password_change, name='account_change_password'),
]
