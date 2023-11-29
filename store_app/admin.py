from django.contrib import admin

from store_app.models import Category, Product, Contact


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'address',)
    search_fields = ('name', 'address',)
