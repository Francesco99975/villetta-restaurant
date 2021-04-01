from django.http import JsonResponse
from .models import Setting
from django.core import serializers


def prefs(request):
    prefs = Setting.objects.all()

    return JsonResponse({
        'settings': serializers.serialize('json', prefs)
    })
