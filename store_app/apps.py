import os

from django.apps import AppConfig
from config.settings import env


class StoreAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store_app"
    verbose_name = 'Магазин'

    catalog_per_page = env.int('STORE_CATALOG_PER_PAGE', 15)
