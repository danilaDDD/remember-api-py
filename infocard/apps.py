from django.apps import AppConfig


class InfoCardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infocard'

    def ready(self):
        import infocard.signals
