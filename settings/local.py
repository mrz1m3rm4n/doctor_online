from .settings_base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'settings/local.cnf'
        }
    }
}

STATIC_ROOT = 'statics'
