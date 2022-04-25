from django.urls import path
from shop.views import *

urlpatterns = [
    path('', products_list, name='product_list')
]