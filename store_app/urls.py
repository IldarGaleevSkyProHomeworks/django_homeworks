from django.urls import path

from store_app.apps import StoreAppConfig
from store_app.views import create_product, ProductDetailView, ProductListView

app_name = StoreAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', create_product, name='create_product'),
]
