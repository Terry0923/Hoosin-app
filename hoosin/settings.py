"""
Django settings for hoosin project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rjabi8oph6=ur^_wz2rnjki%i-u-hq%+=*20%yuf_at_!jc(l1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '769440763457-lmmmdrttl5lfmdtrlun4o44p0f7vf1e7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '1MpnecGGDNVVg13CG_X-56Oz'


LOGIN_URL = '/auth/login/google-oauth2/'

LOGOUT_REDIRECT_URL = ''

LOGIN_REDIRECT_URL = '/profiles/students'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/hoosin/error/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
    'hd': 'virginia.edu'
}

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'profiles.apps.ProfilesConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
#    'social.apps.django_app.default',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
)

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    # 'social_core.pipeline.social_auth.social_details',
    #
    # # Get the social uid from whichever service we're authing thru. The uid is
    # # the unique identifier of the given user in the provider.
    # 'social_core.pipeline.social_auth.social_uid',
    #
    # # Login error pipeline
    # 'project-103-hoosin.pipeline.auth_allowed',
    #
    # # Verifies that the current auth process is valid within the current
    # # project, this is where emails and domains whitelists are applied (if
    # # defined).
    # 'social_core.pipeline.social_auth.auth_allowed',
    #
    # # Checks if the current social-account is already associated in the site.
    # 'social_core.pipeline.social_auth.social_user',
    #
    # # Make up a username for this person, appends a random string at the end if
    # # there's any collision.
    # 'social_core.pipeline.user.get_username',
    #
    # # Send a validation email to the user to verify its email address.
    # # Disabled by default.
    # # 'social_core.pipeline.mail.mail_validation',
    #
    # # Associates the current social details with another user account with
    # # a similar email address. Disabled by default.
    # # 'social_core.pipeline.social_auth.associate_by_email',
    #
    # # Create a user account if we haven't found one yet.
    # 'social_core.pipeline.user.create_user',
    #
    # # Create the record that associates the social account with the user.
    # 'social_core.pipeline.social_auth.associate_user',
    #
    # # Populate the extra_data field in the social record with the values
    # # specified by settings (and the default ones like access_token, etc).
    #'social_core.pipeline.social_auth.load_extra_data',
    #
    # # Update the user record with any changed info from the auth service.
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'hoosin.pipeline.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hoosin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hoosin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.hoosin'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/




MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK='bootstrap4'

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

ALLOWED_HOSTS = ['testcases123.herokuapp.com', 'localhost', '127.0.0.1']

if '/app' in os.environ['HOME']:
    import django_heroku
    django_heroku.settings(locals())
