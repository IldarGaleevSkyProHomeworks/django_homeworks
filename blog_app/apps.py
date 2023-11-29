from django.apps import AppConfig
from config.settings import env


class BlogAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog_app"
    verbose_name = "Блог"

    articles_per_page = env.int('ARTICLES_PER_PAGE', 15)
    article_view_counts_congrats = [int(num) for num in env.list('ARTICLE_VIEW_COUNTS_CONGRATS', [100, 200])]
    article_congrats_mail_subject = env.str('ARTICLE_CONGRATS_MAIL_SUBJECT', "Horns'n'Hoofs · Ваша статья великолепна!")
