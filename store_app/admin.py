from django.contrib import admin

from store_app.models import Category, Product, WordFilter


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


@admin.register(WordFilter)
class WordFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'is_enable')
    list_filter = ('is_enable',)
    search_fields = ('name', 'regular_expression', 'comment',)
