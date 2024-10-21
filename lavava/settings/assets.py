from .base import BASE_DIR

STATICFILES_DIRS = [
    BASE_DIR / "lavava" / "static",
]

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
