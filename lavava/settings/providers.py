import os
from dotenv import load_dotenv

load_dotenv()

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "EMAIL_AUTHENTICATION": True,
        "APP": {
            "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
            "secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
            "key": "",
        },
    }
}

# Regular Accounts
ACCOUNT_EMAIL_REQUIRED = True  # Require email for registration
ACCOUNT_AUTHENTICATION_METHOD = "email"  # Use email to login
ACCOUNT_CHANGE_EMAIL = True  # Limit to one email per account

# Social Accounts
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

SITE_ID = 1
