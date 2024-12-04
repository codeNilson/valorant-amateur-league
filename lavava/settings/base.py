from pathlib import Path
from django.urls import reverse_lazy  # noqa: W0611
from .environment import SECRET_KEY, DEBUG, ALLOWED_HOSTS

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ROOT_URLCONF = "lavava.urls"

WSGI_APPLICATION = "lavava.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "players.Player"

LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGOUT_REDIRECT_URL = reverse_lazy("home")


# All-Auth settings
# Regular Account
ACCOUNT_EMAIL_VERIFICATION = "none"  # Disable email verification
ACCOUNT_EMAIL_REQUIRED = True  # Require email for registration
ACCOUNT_AUTHENTICATION_METHOD = "email"  # Use email to login
ACCOUNT_CHANGE_EMAIL = True  # Limit to one email per account

# Social Accounts
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

SITE_ID = 1
ACCOUNT_SESSION_REMEMBER = True  # Default to optional remember me

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
