import os
from dotenv import load_dotenv
from utils import get_env_list

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG_MODE", "False").lower() in ["true", "1"]

ALLOWED_HOSTS = get_env_list("ALLOWED_HOSTS")

# Django DEBUG Toolbar
INTERNAL_IPS = get_env_list("INTERNAL_IPS")

# Django CORS Headers
CSRF_TRUSTED_ORIGINS = get_env_list("TRUSTED_ORIGINS")
