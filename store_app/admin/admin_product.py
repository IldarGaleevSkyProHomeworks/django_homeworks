from django.contrib import admin

from store_app.admin.admin_product_version import ProductVersionInline
from store_app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'seller')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category',)
    inlines = [
        ProductVersionInline
    ]
