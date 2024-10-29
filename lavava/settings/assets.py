from .base import BASE_DIR

STATICFILES_DIRS = [
    BASE_DIR / "lavava" / "static",
]

STATIC_URL = "static/"
MEDIA_URL = "media/"

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"
