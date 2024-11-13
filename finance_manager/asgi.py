# finance_manager/asgi.py

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_manager.settings')

# Create the ASGI application instance
application = get_asgi_application()
