from datetime import timedelta
import random

import lorem
import pytils.translit
from django.core.management import BaseCommand
from django.utils import timezone

from blog_app.models import Article


class Command(BaseCommand):
    help = 'Creates random articles'

    def handle(self, *args, **options):
        count = options['count']
        articles = []
        for _ in range(count):
            new_title = lorem.get_sentence()
            articles.append(Article(
                title=new_title,
                slug=pytils.translit.slugify(new_title),
                content_text=lorem.get_paragraph(3),
                create_date=timezone.now() - timedelta(hours=random.randint(0, 48)),
                is_published=options['publish'],
            ))

        Article.objects.bulk_create(articles)
        print(f"Created {count} articles")

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            help='Count of articles',
            default=1,
            nargs='?'
        )

        parser.add_argument(
            '-p',
            '--publish',
            action='store_true',
            help='Publish created articles'
        )
