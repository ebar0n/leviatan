# -*- coding: utf-8 -*-
from django.conf import settings

BROKER_URL = settings.BROKER_URL
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = settings.TIME_ZONE
CELERYBEAT_SCHEDULE = {}

if settings.TEST:
    BROKER_BACKEND = 'memory'
    CELERY_ALWAYS_EAGER = True
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
