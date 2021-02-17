from django.db import models
from preferences.models import Preferences


class Contact(Preferences):
    telephone_number = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=300)
    instagram_link = models.CharField(max_length=300)

    monday_opening_time = models.TimeField()
    monday_closing_time = models.TimeField()

    tuesday_opening_time = models.TimeField()
    tuesday_closing_time = models.TimeField()

    wednesday_opening_time = models.TimeField()
    wednesday_closing_time = models.TimeField()

    thursday_opening_time = models.TimeField()
    thursday_closing_time = models.TimeField()

    friday_opening_time = models.TimeField()
    friday_closing_time = models.TimeField()

    saturday_opening_time = models.TimeField()
    saturday_closing_time = models.TimeField()

    sunday_opening_time = models.TimeField()
    sunday_closing_time = models.TimeField()

    def __str__(self):
        return 'Settings'
