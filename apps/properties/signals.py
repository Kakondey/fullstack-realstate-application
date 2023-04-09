from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.properties.models import *
from apps.properties.serializers import *


@receiver(post_save, sender=Property)
def create_photos(sender, instance, created, **kwargs):
    if created:
        photos_data = kwargs.get('photos_data')
        if photos_data:
            photo_serializer = PhotoSerializer(data=photos_data, many=True)
            photo_serializer.is_valid(raise_exception=True)
            photo_serializer.save(property=instance)
