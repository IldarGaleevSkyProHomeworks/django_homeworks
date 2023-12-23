import logging

from background_task import background
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from blog_app.apps import BlogAppConfig
from blog_app.models import Article

logger = logging.getLogger(__name__)


@background()
def task_article_congrats(article_id, view_count=None):
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
