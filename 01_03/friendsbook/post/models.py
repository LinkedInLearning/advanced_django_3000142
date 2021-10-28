from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    content = models.CharField(max_length=140)
    created_on = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.content[0:20])