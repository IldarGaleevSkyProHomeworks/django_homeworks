import os

from django.apps import AppConfig

from config.settings import env

class BlogAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog_app"
    verbose_name = "Блог"

    articles_per_page = env.int('ARTICLES_PER_PAGE', 15)
