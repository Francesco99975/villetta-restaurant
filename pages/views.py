from django.shortcuts import render
from django.http import HttpResponse
from specials.models import Special
from plates.models import Plate


def index(request):
    specials = Special.objects.all()
    plates = Plate.objects.all()

    context = {
        'specials': specials,
        'plates': plates
    }
    return render(request, 'pages/index.html', context)
