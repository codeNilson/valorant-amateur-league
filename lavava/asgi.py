import os
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lavava.settings")


load_dotenv()
application = get_asgi_application()
