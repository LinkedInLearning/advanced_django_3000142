from django.db import models
from django.db.models.deletion import CASCADE
from django.apps import apps
from useraccount.models import UserAccount
from business.models import Business

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class ProfilePage(models.Model):
    user_account = models.ForeignKey(UserAccount, null=True, blank=False, on_delete=CASCADE)
