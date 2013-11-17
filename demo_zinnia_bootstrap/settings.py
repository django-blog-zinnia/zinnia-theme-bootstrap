"""Settings for the zinnia-theme-bootstrap demo"""
import os

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default':
             {'ENGINE': 'django.db.backends.sqlite3',
              'NAME': os.path.join(os.path.dirname(__file__), 'demo.db')}
             }

TIME_ZONE = 'Europe/Paris'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

SECRET_KEY = 'jo-1rzm(%sf)3#n+fb7h945ybv3xpt63abhi12_t7e^^5q8dyw'

USE_TZ = True
USE_I18N = True
USE_L10N = True

SITE_ID = 1

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('de', gettext('German')),
    ('es', gettext('Spanish')),
    ('it', gettext('Italian')),
    ('nl', gettext('Dutch')),
    ('hu', gettext('Hungarian')),
    ('cs', gettext('Czech')),
    ('sk', gettext('Slovak')),
    ('lt', gettext('Lithuanian')),
    ('ru', gettext('Russian')),
    ('pl', gettext('Polish')),
    ('eu', gettext('Basque')),
    ('ca', gettext('Catalan')),
    ('tr', gettext('Turkish')),
    ('hr_HR', gettext('Croatian')),
    ('pt_BR', gettext('Brazilian Portuguese')),
    ('fi_FI', gettext('Finnish (Finland)')),
    ('zh_CN', gettext('Simplified Chinese')),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'demo_zinnia_bootstrap.urls'

TEMPLATE_LOADERS = (
    'app_namespace.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'zinnia.context_processors.version',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'zinnia_bootstrap',
    'mptt',
    'zinnia',
    'tagging',
)
