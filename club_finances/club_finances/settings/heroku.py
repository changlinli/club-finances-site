from club_finances.settings.common import *
import sensitive

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS.append(sensitive.HEROKU_APP_URL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': sensitive.HEROKU_DB_NAME,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': sensitive.HEROKU_DB_USER,
        'PASSWORD': sensitive.HEROKU_DB_PWD,
        'HOST': sensitive.HEROKU_DB_HOST,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': sensitive.HEROKU_DB_PORT,                      # Set to empty string for default.
    }
}

# The following comes form Heroku

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
