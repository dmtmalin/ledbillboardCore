# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROLE = [
        ('lessor', 'Арендодатель'),
        ('tenant', 'Арендатор')
    ]
    username = models.CharField(u'Имя пользователя', max_length=255)
    email = models.EmailField(u'Электронная почта', max_length=255, unique=True, error_messages={
        'unique': 'Пользователь с такой электронной почтой уже существует.',
    })
    role = models.CharField(u'Пол', max_length=6, choices=ROLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ('username',)
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
