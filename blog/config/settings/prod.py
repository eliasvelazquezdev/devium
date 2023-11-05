from .base import *

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