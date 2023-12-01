from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    verbose_name = "Основное"

    popular_product_count = 5
    popular_article_count = 3
