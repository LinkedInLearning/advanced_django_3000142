from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError


# C0FFEE -> 12648430
def hex_to_int(value):
    if value is None:
        return None
    return int(value, 16)

# 12648430 -> C0FFEE
def int_to_hex(value):
    hex_val = format(value, 'X')
    # Pad with 0's, if needed
    hex_val = '0'*(6-len(hex_val)) + hex_val
    return hex_val


class RGBcolorField(models.CharField):
    description = 'A field for holding RGB color values'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



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