import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from dishes.models import Dish
from preferences import Preferences
from django.core import serializers
from carton.cart import Cart


def index(request):
    specials = Dish.objects.all().filter(is_published=True, is_special=True)
    antipasti = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="A")
    primi = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="P")
    secondi = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="S")
    pizze = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="Z")
    desserts = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="D")
    beverages = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="B")

    context = {
        'specials': specials,
        'dishes': {
            'antipasti': antipasti,
            'primi': primi,
            'secondi': secondi,
            'pizze': pizze,
            'desserts': desserts,
            'beverages': beverages,
            'qty': len(antipasti) + len(primi) + len(secondi) + len(pizze) + len(desserts) + len(beverages)
        },
        'checkout': False
    }
    return render(request, 'pages/index.html', context)


def order(request):
    specials = Dish.objects.all().filter(is_published=True, is_special=True)
    antipasti = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="A")
    primi = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="P")
    secondi = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="S")
    pizze = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="Z")
    desserts = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="D")
    beverages = Dish.objects.all().filter(
        is_published=True, is_special=False, course_type="B")

    context = {
        'specials': specials,
        'dishes': {
            'antipasti': antipasti,
            'primi': primi,
            'secondi': secondi,
            'pizze': pizze,
            'desserts': desserts,
            'beverages': beverages,
            'qty': len(antipasti) + len(primi) + len(secondi) + len(pizze) + len(desserts) + len(beverages)
        },
        'checkout': True
    }
    return render(request, 'pages/order.html', context)


def items(request):
    specials = serializers.serialize(
        'json', Dish.objects.all().filter(is_published=True, is_special=True))
    antipasti = serializers.serialize(
        'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="A"))
    primi = serializers.serialize(
        'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="P"))
    secondi = serializers.serialize(
        'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="S"))
    pizze = serializers.serialize(
        'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="Z"))
    desserts = serializers.serialize(
        'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="D"))
    beverages = serializers.serialize(
        'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="B"))

    cart = Cart(request.session)

    return JsonResponse({
        'specials': json.loads(specials),
        'antipasti': json.loads(antipasti),
        'primi': json.loads(primi),
        'secondi': json.loads(secondi),
        'pizze': json.loads(pizze),
        'desserts': json.loads(desserts),
        'beverages': json.loads(beverages),
        'bag-qty': cart.count
    })


def add_to_bag(request, dish_id):
    cart = Cart(request.session)
    dish = Dish.objects.all().get(id=dish_id)
    cart.add(dish, price=dish.price)
    return JsonResponse({
        'message': f'{dish.name} added to Bag!',
        'bag-qty': cart.count
    })


def remove_from_bag(request, dish_id):
    cart = Cart(request.session)
    dish = Dish.objects.all().get(id=dish_id)
    cart.remove(dish)
    return JsonResponse({
        'message': f'{dish.name} removed from Bag!',
        'bag-qty': cart.count
    })


def show_bag(request):
    return render(request, 'pages/bag.html')
