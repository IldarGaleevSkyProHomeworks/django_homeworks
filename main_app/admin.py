from django.contrib import admin

from main_app.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'address',)
    search_fields = ('name', 'address',)