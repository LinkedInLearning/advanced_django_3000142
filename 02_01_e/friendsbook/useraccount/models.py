from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class UserAccount(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=CASCADE)
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    created_on = models.DateTimeField('date created', auto_now_add=True)
    birthday = models.DateField()
    location = models.CharField(max_length=200)
    about = models.TextField(null=True)

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)