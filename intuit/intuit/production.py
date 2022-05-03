from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = False

ALLOWED_HOSTS = ["intuit.kg", "localhost"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'