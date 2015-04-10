# -*- coding: utf-8 -*-
"""
Django settings for narayana project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from settings_local import DEBUG

# gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '83xrbsz4s91di^+&3!)v6bw)!jw2en++j#vdnf5__wznvkc(vo'

# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Fedorov Igor', 'ifedor@ymail.com'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
)

SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'narayana', 'templates'),
)

# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'easy_thumbnails',
    'captcha',
    'ifcropper',
    'news',
    'feedback',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

# ifcropper thumbnails
from easy_thumbnails.conf import Settings as thumbnail_settings
IMAGE_CROPPING_THUMB_SIZE = (300, 300)
IMAGE_CROPPING_SIZE_WARNING = True
THUMBNAIL_PROCESSORS = (
    'ifcropper.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

TINYMCE_DEFAULT_CONFIG = {
    # 'file_browser_callback': "djangoFileBrowser",
    'file_browser_callback': 'mce_filebrowser',
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'width': 850,
    'height': 400,
}

ROOT_URLCONF = 'narayana.urls'

WSGI_APPLICATION = 'narayana.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

LANGUAGES = (
    # # Customize this
    ('ru', u'Русский'),

)

CMS_LANGUAGES = {
    # # Customize this
    'default': {
        'hide_untranslated': False,
        'redirect_on_fallback': True,
        'public': True,
    },
    1: [
        {
            'redirect_on_fallback': True,
            'code': 'ru',
            'hide_untranslated': False,
            'name': u'Русский',
            'public': True,
        },

    ],
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

CMS_TEMPLATES = (
    # # Customize this
    ('page.html', 'Main Page'),
    ('inner.html', 'Inner Page')
)

CMS_PERMISSION = False

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': u'narayana',
            'HOST': u'localhost',
            'USER': u'narayana',
            'PASSWORD': u'123456',
            'PORT': ''
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'narayana', 'static'),
)

if DEBUG:
    try:
        from settings_local import *
    except ImportError:
        pass
