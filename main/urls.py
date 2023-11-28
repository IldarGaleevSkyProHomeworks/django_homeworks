from django.urls import path

from main.views import index, catalog, contacts, create_product, product_info

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:product_id>/', product_info, name='product'),
    path('contacts', contacts, name='contacts'),
    path('create_product', create_product, name='create_product'),
]
