from django.contrib import admin

from main.models import Category, Product


# Register your models here.

@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', 'description', )


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', )
    list_filter = ('category', )
    search_fields = ('name', 'description', 'category', )
