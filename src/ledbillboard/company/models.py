from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    name = models.CharField(_('Company name'), max_length=255)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name
