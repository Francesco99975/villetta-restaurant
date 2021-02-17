from django.contrib import admin
from preferences.admin import PreferencesAdmin
from .models import Setting

admin.site.register(Setting, PreferencesAdmin)
