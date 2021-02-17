from django.contrib import admin
from preferences.admin import PreferencesAdmin
from .models import Contact


class ContactAdmin(PreferencesAdmin):
    list_display = ('email', 'telephone_number')

    list_display_links = ('email', 'telephone_number')


admin.site.register(Contact, ContactAdmin)
