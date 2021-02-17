from django.shortcuts import render
from django.http import HttpResponse
from specials.models import Special
from plates.models import Plate
from preferences import Preferences


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
        }
    }
    return render(request, 'pages/index.html', context)
