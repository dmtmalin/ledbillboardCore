# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(_('Full name'), max_length=255)
    email = models.EmailField(_('E-mail'), max_length=255, unique=True, error_messages={
        'unique': _('The user with such e-mail already exists.'),
    })
    phone = models.CharField(_('Phone'), max_length=20, null=True, blank=True, validators=[
        validators.RegexValidator(
            r'^\+[1-9]{1}[0-9]{3,14}$',
            _('Phone in international format.')
        ),
    ])
    birthday = models.DateTimeField(_('Birthday'), null=True, blank=True)
    is_lessor = models.BooleanField(_('Lessor status'), default=False,
                                    help_text=_('Designates whether this user should be treated as lessor.'))
    company = models.OneToOneField('company.Company', verbose_name=_('Company'), blank=True, null=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
