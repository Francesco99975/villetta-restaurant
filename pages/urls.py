from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('order', views.order, name="order"),
    path('items', views.items, name="items"),
    path('add-to-bag/<int:dish_id>',
         views.add_to_bag, name="add-to-bag"),
    path('remove-from-bag', views.remove_from_bag, name="remove-from-bag"),
    path('bag', views.show_bag, name="bag")
]
