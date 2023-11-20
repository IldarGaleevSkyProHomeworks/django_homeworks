import os

from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
    verbose_name = 'Магазин'

    catalog_per_page = os.getenv('MAIN_CATALOG_PER_PAGE', 15)
