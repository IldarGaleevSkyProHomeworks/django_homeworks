from django.conf import settings
from django.urls import path
from django.views.decorators.cache import cache_page

from store_app.apps import StoreAppConfig
from store_app.views import ProductCreateView, ProductUpdateView, ProductDetailView, ProductListView

app_name = StoreAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('<int:pk>/', cache_page(settings.PAGE_CACHE_TIME)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
]
