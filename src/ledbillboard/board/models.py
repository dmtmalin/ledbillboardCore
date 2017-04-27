# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Board(models.Model):
    company = models.ForeignKey('company.Company', verbose_name=_('Company'))
    name = models.CharField(_('Name'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=255)
    lat = models.FloatField(_('Latitude'), blank=True, null=True)
    lon = models.FloatField(_('Longitude'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Billboard')
        verbose_name_plural = _('Billboards')
        unique_together = ('name', 'slug', )
