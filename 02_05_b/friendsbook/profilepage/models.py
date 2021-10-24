from django.db import models
from django.db.models.deletion import CASCADE
from django.apps import apps
from useraccount.models import UserAccount
from business.models import Business

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class ProfilePage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    subject = GenericForeignKey('content_type', 'object_id')


