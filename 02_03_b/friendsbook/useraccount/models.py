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
        kwargs['max_length'] = 6
        self._validators = []
        self.validators.append(self.validate_all_values_hex)
        super().__init__(*args, **kwargs)

    def validate_all_values_hex(self, value):
        try:
            hex_to_int(value)
        except: 
            raise ValidationError('{} is not a hex value'.format(value))

    def db_type(self, connection):
        return 'UNSIGNED INTEGER(3)'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None 
        return int_to_hex(value)
    
    def get_prep_value(self, value):
        return hex_to_int(value)


class UserAccount(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=CASCADE)
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    created_on = models.DateTimeField('date created', auto_now_add=True)
    birthday = models.DateField()
    location = models.CharField(max_length=200)
    favorite_color = RGBcolorField(null=True)
    about = models.TextField(null=True)

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)