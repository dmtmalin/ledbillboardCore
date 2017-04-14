from django.db import models


# Create your models here.
from fancy_cronfield.fields import CronField

from ledbillboard.profileauth.models import User


class Playlist(models.Model):
    user = models.ForeignKey(User)


class Schedule(models.Model):
    playlist = models.ForeignKey(Playlist)
    timing = CronField()


class MediaItem(models.Model):
    playlist = models.ForeignKey(Playlist)
    file = models.FileField()
