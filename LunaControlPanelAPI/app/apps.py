from django.apps import AppConfig
from .luna.luna import lunanode

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lunanode'

    def ready(self):
        # Access the singleton instance to ensure it gets initialized
        instance = lunanode
