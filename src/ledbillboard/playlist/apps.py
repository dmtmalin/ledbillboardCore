# -*- coding: utf-8 -*-
from django.apps import AppConfig


class PlaylistConfig(AppConfig):
    name = 'ledbillboard.playlist'

    def ready(self):
        import ledbillboard.playlist.signals
