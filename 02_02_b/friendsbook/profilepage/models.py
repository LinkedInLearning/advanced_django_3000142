from django.db import models
from django.db.models.deletion import CASCADE
from django.apps import apps
from useraccount.models import UserAccount
from business.models import Business

from django.contrib.contenttypes.models import ContentType



class ProfilePage(models.Model):
    user_account = models.ForeignKey(UserAccount, null=True, blank=False, on_delete=CASCADE)

    def __str__(self):
        return '{}'.format(self.user_account.first_name)