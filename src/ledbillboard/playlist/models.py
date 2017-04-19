# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Playlist(models.Model):
    schedule = models.ForeignKey('references.Schedule', verbose_name=_('Schedule'))
    board = models.ForeignKey('board.Board', verbose_name=_('Billboard'))
    media = models.ManyToManyField('mediacontent.Media', verbose_name=_('Media items'), blank=True)

    def __str__(self):
        return self.board.name

    class Meta:
        verbose_name = _('Playlist')
        verbose_name_plural = _('Playlist items')
