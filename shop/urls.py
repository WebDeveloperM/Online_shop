

from django.urls import path
from shop.views import *

urlpatterns = [
    path('', products_list, name='product_list'),
    path('cart/', cart, name='cart'),
    path('delete_cart_item/<int:pk>', delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', edit_cart_item, name='edit_cart_item'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('cart/create_order', create_order, name='create_order'),

    path('rate_product/<int:pk>', rate_product, name='rate_product'),

]