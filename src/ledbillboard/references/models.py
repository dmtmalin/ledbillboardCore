import re

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


def validate_cron(value):
    if value.strip() != value:
        raise ValidationError(_('Leading nor trailing spaces are allowed.'))
    columns = value.split()
    if columns != value.split(' '):
        raise ValidationError(_('Use only a single space as a column separator.'))

    if len(columns) != 5:
        raise ValidationError(_('Entry has to consist of exactly 5 columns.'))

    pattern = r'^(\*|\d+(-\d+)?(,\d+(-\d+)?)*)(/\d+)?$'
    p = re.compile(pattern)
    for i, c in enumerate(columns):
        if not p.match(c):
            message = _('Incorrect value %(value)s in column %(column)d.') % {
                'value': c,
                'column': i+1
            }
            raise ValidationError(message)


class Schedule(models.Model):
    cron = models.CharField(_('Cron command'), max_length=120, validators=[validate_cron, ],
                            help_text=_('0 * * * * that run in every hour.'))
    description = models.CharField(_('Description'), max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')
