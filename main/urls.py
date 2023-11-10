from django.urls import path

from main.views import index, catalog, contacts

urlpatterns = [
    path('', index, name='index'),
    path('catalog', catalog, name='catalog'),
    path('contacts', contacts, name='contacts'),
]
