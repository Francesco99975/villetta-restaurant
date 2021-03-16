import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from specials.models import Special
from plates.models import Plate
from preferences import Preferences
from django.core import serializers


def index(request):
    specials = Special.objects.all().filter(is_published=True)
    antipasti = Plate.objects.all().filter(is_published=True, course_type="A")
    primi = Plate.objects.all().filter(is_published=True, course_type="P")
    secondi = Plate.objects.all().filter(is_published=True, course_type="S")
    pizze = Plate.objects.all().filter(is_published=True, course_type="Z")
    desserts = Plate.objects.all().filter(is_published=True, course_type="D")
    beverages = Plate.objects.all().filter(is_published=True, course_type="B")

    context = {
        'specials': specials,
        'plates': {
            'antipasti': antipasti,
            'primi': primi,
            'secondi': secondi,
            'pizze': pizze,
            'desserts': desserts,
            'beverages': beverages
        },
        'checkout': False
    }
    return render(request, 'pages/index.html', context)


def order(request):
    specials = Special.objects.all().filter(is_published=True)
    antipasti = Plate.objects.all().filter(is_published=True, course_type="A")
    primi = Plate.objects.all().filter(is_published=True, course_type="P")
    secondi = Plate.objects.all().filter(is_published=True, course_type="S")
    pizze = Plate.objects.all().filter(is_published=True, course_type="Z")
    desserts = Plate.objects.all().filter(is_published=True, course_type="D")
    beverages = Plate.objects.all().filter(is_published=True, course_type="B")

    context = {
        'specials': specials,
        'plates': {
            'antipasti': antipasti,
            'primi': primi,
            'secondi': secondi,
            'pizze': pizze,
            'desserts': desserts,
            'beverages': beverages
        },
        'checkout': True
    }
    return render(request, 'pages/order.html', context)


def items(request):
    specials = serializers.serialize(
        'json', Special.objects.all().filter(is_published=True))
    antipasti = serializers.serialize(
        'json', Plate.objects.all().filter(is_published=True, course_type="A"))
    primi = serializers.serialize(
        'json', Plate.objects.all().filter(is_published=True, course_type="P"))
    secondi = serializers.serialize(
        'json', Plate.objects.all().filter(is_published=True, course_type="S"))
    pizze = serializers.serialize(
        'json', Plate.objects.all().filter(is_published=True, course_type="Z"))
    desserts = serializers.serialize(
        'json', Plate.objects.all().filter(is_published=True, course_type="D"))
    beverages = serializers.serialize(
        'json', Plate.objects.all().filter(is_published=True, course_type="B"))

    return JsonResponse({
        'specials': json.loads(specials),
        'antipasti': json.loads(antipasti),
        'primi': json.loads(primi),
        'secondi': json.loads(secondi),
        'pizze': json.loads(pizze),
        'desserts': json.loads(desserts),
        'beverages': json.loads(beverages)
    })
