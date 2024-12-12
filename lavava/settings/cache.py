CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 60, 
        "OPTIONS": {"MAX_ENTRIES": 500},
    }
}
