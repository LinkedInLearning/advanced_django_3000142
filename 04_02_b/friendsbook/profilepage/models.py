from django.db import models
from django.db.models.deletion import CASCADE
from django.apps import apps

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from useraccount.models import UserAccount
from business.models import Business

from django.dispatch import receiver 
from django.db.models.signals import post_save 

class ProfilePage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    subject = GenericForeignKey('content_type', 'object_id')


@receiver(post_save, sender=UserAccount)
def create_profile_user(instance, created, **kwargs):
    if created:
        ProfilePage.objects.create(subject=instance)

@receiver(post_save, sender=Business)
def create_profile_business(instance, created, **kwargs):
    if created:
        ProfilePage.objects.create(subject=instance)   
