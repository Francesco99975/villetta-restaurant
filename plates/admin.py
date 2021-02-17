from django.contrib import admin
from .models import Plate


class PlateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published', 'course_type')

    list_display_links = ('id', 'name')

    list_filter = ('price', )

    list_editable = ('is_published', 'course_type')

    search_fields = ('name', 'description')

    list_per_page = 10


admin.site.register(Plate, PlateAdmin)
