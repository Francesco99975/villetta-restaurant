from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('order', views.order, name="order"),
    path('items', views.items, name="items"),
    path('cart-items', views.cart_items, name="cart_items"),
    path('add-to-bag/<int:dish_id>',
         views.add_to_bag, name="add-to-bag"),
    path('remove-from-bag/<int:dish_id>',
         views.remove_from_bag, name="remove-from-bag"),
    path('clear-bag', views.clear_bag, name="clear_bag"),
    path('bag', views.show_bag, name="bag")
]
