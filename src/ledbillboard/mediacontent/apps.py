from django.apps import AppConfig


class MediacontentConfig(AppConfig):
    name = 'ledbillboard.mediacontent'

    def ready(self):
        import ledbillboard.mediacontent.signals
