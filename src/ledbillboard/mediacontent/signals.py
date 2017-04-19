# coding=utf-8
from django.db.models.signals import post_save
from django.dispatch import receiver

from ledbillboard.mediacontent.models import Media
from ledbillboard.mediacontent.tasks import SaveMediaMetadata


@receiver(post_save, sender=Media)
def save_metadata(sender, instance, created, **kwargs):
    if created:
        SaveMediaMetadata(instance).start()
