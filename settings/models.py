from django.db import models
from preferences.models import Preferences
from datetime import datetime
from django.utils import timezone


class Setting(Preferences):
    telephone_number = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=300)
    instagram_link = models.CharField(max_length=300)
    home_delivery_available = models.BooleanField(default=True)

    monday_opening_time = models.TimeField(default=timezone.now)
    monday_closing_time = models.TimeField(default=timezone.now)

    tuesday_opening_time = models.TimeField(default=timezone.now)
    tuesday_closing_time = models.TimeField(default=timezone.now)

    wednesday_opening_time = models.TimeField(default=timezone.now)
    wednesday_closing_time = models.TimeField(default=timezone.now)

    thursday_opening_time = models.TimeField(default=timezone.now)
    thursday_closing_time = models.TimeField(default=timezone.now)

    friday_opening_time = models.TimeField(default=timezone.now)
    friday_closing_time = models.TimeField(default=timezone.now)

    saturday_opening_time = models.TimeField(default=timezone.now)
    saturday_closing_time = models.TimeField(default=timezone.now)

    sunday_opening_time = models.TimeField(default=timezone.now)
    sunday_closing_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return 'Settings'
