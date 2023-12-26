from django.contrib import admin

from accounts_app.models import User


@admin.register(User)
class NewUserAdmin(admin.ModelAdmin):
    exclude = ('password',)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
