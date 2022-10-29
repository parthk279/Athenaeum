"""
Django app configuration
"""
from django.apps import AppConfig


class AthenaeumConfig(AppConfig):
    """ Class for app config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'athenaeum'
