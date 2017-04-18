# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class NamesValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+$'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, last_name, email, password, **extra_fields):
        if not first_name:
            raise ValueError('Users must have an first name')
        if not last_name:
            raise ValueError('Users must have an last name')
        if not email:
            raise ValueError('Users must have an email address')
        first_name = self.model.normalize_username(first_name)
        last_name = self.model.normalize_username(last_name)
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(first_name, last_name, email, password, **extra_fields)

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(first_name, last_name, email, password, **extra_fields)


class User(AbstractUser):
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
    first_name = models.CharField(_('First name'),  max_length=32, validators=[
        NamesValidator(message=_('Enter a valid first name. This value may contain only letters.')),
    ])
    last_name = models.CharField(_('Last name'),  max_length=32, validators=[
        NamesValidator(message=_('Enter a valid last name. This value may contain only letters.')),
    ])
    is_lessor = models.BooleanField(_('Lessor status'), default=False,
                                    help_text=_('Designates whether this user should be treated as lessor.'))

    username = None
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('first_name', 'last_name', )
        verbose_name = _('User')
        verbose_name_plural = _('Users')
