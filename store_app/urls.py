from django.urls import path

from store_app.apps import StoreAppConfig
from store_app.views import create_product, ProductDetailView, ProductListView

app_name = StoreAppConfig.name

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create_product', create_product, name='create_product'),
]
