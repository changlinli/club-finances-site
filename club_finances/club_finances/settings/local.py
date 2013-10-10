from club_finances.settings.common import *
import sensitive

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS.append('localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': sensitive.LOCAL_DB_NAME,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': sensitive.LOCAL_DB_USER,
        'PASSWORD': sensitive.LOCAL_DB_PWD,
        'HOST': sensitive.HEROKU_DB_HOST,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': sensitive.HEROKU_DB_PORT,                      # Set to empty string for default.
    }
}

