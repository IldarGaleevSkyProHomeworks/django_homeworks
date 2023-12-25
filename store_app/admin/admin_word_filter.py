from django.contrib import admin

from store_app.models import WordFilter


@admin.register(WordFilter)
class WordFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'is_enable')
    list_filter = ('is_enable',)
    search_fields = ('name', 'regular_expression', 'comment',)
