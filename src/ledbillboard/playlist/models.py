# -*- coding: utf-8 -*-
from django.db import models
from fancy_cronfield.fields import CronField
from django.utils.translation import ugettext_lazy as _


class Media(models.Model):
    file = models.FileField(_('File'))
    duration = models.FloatField(_('Duration'), default=0)
    user = models.ForeignKey('account.User', verbose_name=_('User'))
    create_at = models.DateTimeField(_('Upload time'), auto_now_add=True)
    is_approve = models.BooleanField(_('Is approve'), default=False)

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media items')


class Playlist(models.Model):
    board = models.ForeignKey('board.Board', verbose_name=_('Billboard'))
    media = models.ManyToManyField('Media', verbose_name=_('Media items'))
    timing = CronField(_('Schedule'))

    def __str__(self):
        return self.board.name

    class Meta:
        verbose_name = _('Playlist')
        verbose_name_plural = _('Playlist items')
