from django.db import models
from django.utils.translation import ugettext_lazy as _


class Media(models.Model):
    user = models.ForeignKey('account.User', verbose_name=_('User'))
    file = models.FileField(_('File'))
    duration = models.FloatField(_('Duration'), default=0)
    create_at = models.DateTimeField(_('Upload time'), auto_now_add=True)
    is_approve = models.BooleanField(_('Is approve'), default=False)

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media items')
