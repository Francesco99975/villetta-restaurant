from django.db import models
from preferences.models import Preferences


class Contact(Preferences):
    telephone_number = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=300)
    instagram_link = models.CharField(max_length=300)
