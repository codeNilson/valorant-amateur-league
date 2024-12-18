import os
from dotenv import load_dotenv

load_dotenv()


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

ACCOUNT_DEFAULT_HTTP_PROTOCOL = os.environ.get("DEFAULT_HTTP_PROTOCOL", "http")
