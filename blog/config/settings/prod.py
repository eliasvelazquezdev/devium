from .base import *
import dj_database_url

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': dj_database_url.config(
        default = env('DATABASE_URL')
    )
}

if not DEBUG:
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": "rest_framework.renderers.JSONRenderer",
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
        'DEFAULT_PAGINATION_CLASS': 'drf_link_header_pagination.LinkHeaderPagination',
        'PAGE_SIZE': 10,
    }

# List of supported API versions
DRF_VERSIONING_SETTINGS = {
    "VERSION_LIST" : "blog.versioning.version_list.VERSIONS",
    "DEFAULT VERSION": "latest",
}