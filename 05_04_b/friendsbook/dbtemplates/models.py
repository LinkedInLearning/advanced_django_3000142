from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class DBTemplate(models.Model):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=CASCADE)
    content = models.TextField(null=True)

