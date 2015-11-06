"""
Django settings for Bachinit project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
ROOT_DIR = dirname(BASE_DIR)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
MEDIA_URL = "/media/"

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.core.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',

    'corsheaders',
    'gunicorn',

    'accounts',
    'recipes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SITE_ID = 1
ROOT_URLCONF = 'brewabl.urls'
WSGI_APPLICATION = 'brewabl.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Authentication Settings
AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_FORMS = {
    'signup': 'accounts.forms.SignupForm'
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'accounts.serializers.LoginSerializer',
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
}


# Django Rest Framework config
REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGE_SIZE': 50
}

CORS_ORIGIN_ALLOW_ALL = True

# Email config
try:
    from Bachinit.settings.credentials import EMAIL_USER, EMAIL_PASSWORD
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_SSL = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = EMAIL_USER
    EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
except ImportError:
    print('Credentials file not found, falling back to console email backend')
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST_USER = 'user'
    EMAIL_HOST_PASSWORD = 'password'
