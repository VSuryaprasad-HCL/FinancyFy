# finance_manager/settings.py

# finance_manager/settings.py

STATIC_URL = '/static/'

# For production, you can use the following settings:
STATICFILES_DIRS = [BASE_DIR / "static"]

# In case you are deploying on production, use this for static files collection:
# python manage.py collectstatic


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finance_manager_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
