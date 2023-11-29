from django.urls import path

from store_app.apps import StoreAppConfig
from store_app.views import index, catalog, create_product, ProductDetailView, ContactListView

app_name = StoreAppConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('contacts', ContactListView.as_view(), name='contacts'),
    path('create_product', create_product, name='create_product'),
]
