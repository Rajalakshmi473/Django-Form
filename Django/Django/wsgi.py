"""
WSGI config for Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to point to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

# Replace 'Django' with the name of your Django project directory
application = get_wsgi_application()
