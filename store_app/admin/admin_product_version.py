from django.contrib import admin

from store_app.models import ProductVersion


class ProductVersionInline(admin.StackedInline):
    model = ProductVersion
    extra = 1


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'product', 'version_number')
    list_filter = ('is_latest',)
    search_fields = ('version_name', 'product', 'version_number',)
