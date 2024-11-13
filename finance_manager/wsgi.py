# finance_manager/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_manager.settings')

# Create the WSGI application that can be used by the web 
