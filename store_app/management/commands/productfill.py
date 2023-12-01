import random

from django.core.management import BaseCommand
from django.core.management import call_command

from store_app.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category1 = Category(name='Бакалея')
        category2 = Category(name='Напитки')

        categories = [category1, category2]

        products = [
            Product(
                name='Товар с очень длинным, до невозможности, названием',
                description='Описание у товара тоже достаточно длинное. '
                            'Вот прям постарались дать подробное описание, '
                            'которое, возможно, и читать никто не станет. '
                            'Но лучше пусть будет',
                price=100500.99,
                category=category1
            ),
            Product(name='Рис', price=111.90, category=category1),
            Product(name='Крупа гречневая', price=55.90, category=category1),
            Product(name='Макароны - спагетти', price=39.90, category=category1),
            Product(name='Сок яблочный', price=15.99, category=category2),
            Product(name='Сок персиковый', price=119.99, category=category2),
            Product(name='Сок апельсиновый', price=47.99, category=category2),
        ]

        for n in range(100):
            products.append(Product(name=f'Product {n}', price=random.random() * n, category=random.choice(categories)))

        Category.objects.bulk_create(categories)
        Product.objects.bulk_create(products)
