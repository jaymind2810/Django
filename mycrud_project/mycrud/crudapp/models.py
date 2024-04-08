from django.db import models
from datetime import datetime
# from multiselectfield import MultiSelectField


class RegistrationForm(models.Model):


    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    email = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_choices, max_length=10, default='male')
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=25)
    address = models.TextField()