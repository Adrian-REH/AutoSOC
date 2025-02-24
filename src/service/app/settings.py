import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'clave-super-secreta')

DEBUG = os.getenv('DEBUG', 'False') == 'True'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "payments",
    "items",
    "actions",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Cambia a PostgreSQL en producción
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Opcional, si tienes una carpeta de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ← Necesario para Admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ← Necesario para Admin
    'django.contrib.messages.middleware.MessageMiddleware',  # ← Necesario para Admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

ROOT_URLCONF = 'app.urls'

