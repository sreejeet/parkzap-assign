from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    if not str(value).isdigit()\
            or len(str(value)) < 10\
            or len(str(value)) > 12\
            or int(value) < 0:
        raise ValidationError(
            _('%(value)s is not a valid phone number'),
            params={'value': value},
        )


class UserData(models.Model):
    name = models.CharField(max_length=256, help_text='Your name')
    email = models.EmailField(max_length=256, help_text='Your email address')
    dob = models.DateField(help_text='Your date of birth')
    phone = models.CharField(max_length=12,
                             help_text='Your phone',
                             validators=[validate_phone])

    def __str__(self):
        return self.name
