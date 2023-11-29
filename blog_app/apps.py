import os

from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog_app"
    verbose_name = "Блог"

    articles_per_page = os.getenv('ARTICLES_PER_PAGE', 15)
