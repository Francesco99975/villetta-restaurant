import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from dishes.models import Dish
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from carton.cart import Cart


# def index(request):
#     specials = Dish.objects.all().filter(is_published=True, is_special=True)
#     antipasti = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="A")
#     primi = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="P")
#     secondi = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="S")
#     pizze = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="Z")
#     desserts = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="D")
#     beverages = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="B")

#     context = {
#         'specials': specials,
#         'dishes': {
#             'antipasti': antipasti,
#             'primi': primi,
#             'secondi': secondi,
#             'pizze': pizze,
#             'desserts': desserts,
#             'beverages': beverages,
#             'qty': len(antipasti) + len(primi) + len(secondi) + len(pizze) + len(desserts) + len(beverages)
#         },
#         'checkout': False
#     }
#     return render(request, 'pages/index.html', context)

def index(request):
    return redirect('/admin')


# def order(request):
#     specials = Dish.objects.all().filter(is_published=True, is_special=True)
#     antipasti = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="A")
#     primi = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="P")
#     secondi = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="S")
#     pizze = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="Z")
#     desserts = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="D")
#     beverages = Dish.objects.all().filter(
#         is_published=True, is_special=False, course_type="B")

#     context = {
#         'specials': specials,
#         'dishes': {
#             'antipasti': antipasti,
#             'primi': primi,
#             'secondi': secondi,
#             'pizze': pizze,
#             'desserts': desserts,
#             'beverages': beverages,
#             'qty': len(antipasti) + len(primi) + len(secondi) + len(pizze) + len(desserts) + len(beverages)
#         },
#         'checkout': True
#     }
#     return render(request, 'pages/order.html', context)


def items(request):
    if not request.session or not request.session.session_key:
        print("Saving Session")
        request.session.save()
    # specials = serializers.serialize(
    #     'json', Dish.objects.all().filter(is_published=True, is_special=True))
    # antipasti = serializers.serialize(
    #     'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="A"))
    # primi = serializers.serialize(
    #     'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="P"))
    # secondi = serializers.serialize(
    #     'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="S"))
    # pizze = serializers.serialize(
    #     'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="Z"))
    # desserts = serializers.serialize(
    #     'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="D"))
    # beverages = serializers.serialize(
    #     'json', Dish.objects.all().filter(is_published=True, is_special=False, course_type="B"))

    cart = Cart(request.session)

    return JsonResponse({
        # 'specials': json.loads(specials),
        # 'antipasti': json.loads(antipasti),
        # 'primi': json.loads(primi),
        # 'secondi': json.loads(secondi),
        # 'pizze': json.loads(pizze),
        # 'desserts': json.loads(desserts),
        # 'beverages': json.loads(beverages),
        'dishes': json.loads(serializers.serialize('json', Dish.objects.all().filter(is_published=True)))
    })


def cart_items(request):
    cart = Cart(request.session)
    return JsonResponse({
        'cart': json.dumps(list(map(lambda x: x[1], cart.items_serializable))),
        'dishes': json.loads(serializers.serialize('json', Dish.objects.all().filter(is_published=True)))
    })


@csrf_exempt
def add_to_bag(request, dish_id):
    if request.method == 'GET':
        cart = Cart(request.session)
        dish = Dish.objects.all().get(id=dish_id)
        cart.add(dish, price=dish.price)
        return JsonResponse({
            'message': f'{dish.name} added to Bag!',
            'bag-qty': cart.count
        })
    elif request.method == 'POST':
        item_quantity = JSONParser().parse(request)['quantity']
        cart = Cart(request.session)
        dish = Dish.objects.all().get(id=dish_id)
        cart.add(dish, price=dish.price, quantity=item_quantity)
        return JsonResponse({
            'message': f'{dish.name} added to Bag!',
        })


@csrf_exempt
def remove_from_bag(request, dish_id):
    cart = Cart(request.session)
    dish = Dish.objects.all().get(id=dish_id)
    cart.remove(dish)
    return JsonResponse({
        'message': f'{dish.name} removed from Bag!',
        'bag-qty': cart.count
    })


def clear_bag(request):
    cart = Cart(request.session)
    cart.clear()
    return JsonResponse({
        'message': 'Bag Cleared!',
        'bag-qty': cart.count
    })


def show_bag(request):
    return render(request, 'pages/bag.html')
