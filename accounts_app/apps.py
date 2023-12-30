from django.apps import AppConfig

from config.settings import env


class AccountsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts_app"
    verbose_name = 'Аккаунты'

    verify_mail_mail_subject = env.str('VERIFY_MAIL_MAIL_SUBJECT', "Horns'n'Hoofs · Подтверждение адреса почты")
