import os
from dotenv import load_dotenv
from lavava.settings import BASE_DIR

load_dotenv()

EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND")
EMAIL_FILE_PATH = BASE_DIR / "emails"
DEFAULT_FROM_EMAIL = 'no-reply@lavava.com'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
