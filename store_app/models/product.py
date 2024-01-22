from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts_app.models import User
from utils.hash_storage import product_preview_images, HashStorage
from utils.const import MF_NULL

from store_app.models.product_category import Category


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1024, verbose_name='описание', **MF_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена', default=0.0)
    create_date = models.DateTimeField(verbose_name='дата создания', default=timezone.now)
    modify_date = models.DateTimeField(verbose_name='дата изменения', default=timezone.now)
    preview_image = models.ImageField(upload_to=product_preview_images, storage=HashStorage(),
                                      verbose_name='изображение', **MF_NULL)  # 'product_preview_images/'

    seller = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='products',
                               verbose_name='Продавец', **MF_NULL)

    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    def __str__(self):
        return f'{self.name}: {self.price:.3}'

    def get_absolute_url(self):
        return reverse('store_app:product', kwargs={'pk': self.pk})

    @property
    def active_version(self):
        if not settings.CACHE_ENABLED:
            return self.versions.filter(is_latest=True).first()
        return cache.get_or_set(
            key=f'product_{self.pk}_version',
            default=self.versions.filter(is_latest=True).first(),

            # TODO: need timeout config manager
            # timeout=30
        )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name', 'price', 'create_date', 'modify_date', 'category',)
        permissions = [
            ('can_unpublished_product', 'Может отменять публикацию продукта'),
            ('can_change_product_name', 'Может изменять название продукта'),
            ('can_change_product_description', 'Может изменять описание продукта'),
            ('can_change_product_category', 'Может изменять категорию продукта'),
        ]
