# Ainity/asgi.py
import os
from channels.routing import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ainity.settings')
application = get_asgi_application()
