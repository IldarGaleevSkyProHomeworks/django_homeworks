import logging

from background_task import background
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts_app.models import User
from blog_app.apps import BlogAppConfig
from accounts_app.apps import AccountsAppConfig
from blog_app.models import Article

logger = logging.getLogger(__name__)


@background()
def task_article_congrats(article_id, site_id, view_count=None):
    article = Article.objects.filter(pk=article_id).first()

    logger.debug(f'Article {article_id} view {view_count}')

    if not article:
        logger.warning('Wrong article id')
        return

    if article.author_email:
        view_count = view_count if view_count else article.view_count

        ctx = {
            'object': article,
            'view_count': view_count
        }

        html_body = render_to_string('email/article_congrats.html', context=ctx)

        msg = EmailMultiAlternatives(
            subject=BlogAppConfig.article_congrats_mail_subject,
            to=[article.author_email]
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()

        logger.debug(f'Send mail to {article.author_email} complete')
    else:
        logger.debug('Article author email not specified')


@background
def send_email_to_verify(user_id: int, site_id: int):
    try:
        user = User.objects.get(pk=user_id)
        site = Site.objects.get(pk=site_id)

        uid_b64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        domain_name = site.domain
        domain_scheme = 'http'  # TODO: hardcoded scheme!
        uri = reverse('accounts:email_verify', kwargs={'uidb64': uid_b64, 'token': token})

        ctx = {
            'user': user,
            'email_verify_uri': f"{domain_scheme}://{domain_name}{uri}",
        }

        html_body = render_to_string('email/email_verify.html', context=ctx)

        msg = EmailMultiAlternatives(
            subject=AccountsAppConfig.verify_mail_mail_subject,
            to=[user.email]
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()

        logger.debug(f'Send verify mail to {user.email} complete')

    except Exception as e:
        logger.error(e)


@background
def send_new_user_password(user_id: int, new_password: str, site_id: int):
    try:
        user = User.objects.get(pk=user_id)
        site = Site.objects.get(pk=site_id)

        ctx = {
            'user': user,
            'new_password': new_password,
        }

        html_body = render_to_string('email/email_reset_password.html', context=ctx)

        msg = EmailMultiAlternatives(
            subject=AccountsAppConfig.reset_password_mail_subject,
            to=[user.email]
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()

        logger.debug(f'Send new password mail to {user.email} complete')

    except Exception as e:
        logger.error(e)
