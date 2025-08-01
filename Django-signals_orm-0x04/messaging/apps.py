from django.apps import AppConfig


class ChatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messaging'

    # to import the signals when the app is ready
    def ready(self): #is ready a built in method ende tadya?
        import messaging.signals
