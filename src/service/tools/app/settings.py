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
    'corsheaders',
    "items",
    "actions",
    "user_sessions",
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
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ← Necesario para Admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ← Necesario para Admin
    'django.contrib.messages.middleware.MessageMiddleware',  # ← Necesario para Admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
USER_EMAIL = os.getenv("USER_EMAIL")
PASS_APP_EMAIL= os.getenv("PASS_APP_EMAIL")

CORS_ALLOW_ALL_ORIGINS  = True
ROOT_URLCONF = 'app.urls'


NGINX_BLOCKLIST = "blocked_ips.conf"
HOST_RABBITMQ = os.getenv("HOST_RABBITMQ")

if not os.path.exists(NGINX_BLOCKLIST):
	open(NGINX_BLOCKLIST, "w").close()  # Crea el archivo vacío si no existe
