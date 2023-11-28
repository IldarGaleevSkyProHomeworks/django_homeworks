import os

from django.apps import AppConfig


class StoreAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store_app"
    verbose_name = 'Магазин'

    catalog_per_page = os.getenv('STORE_CATALOG_PER_PAGE', 15)
