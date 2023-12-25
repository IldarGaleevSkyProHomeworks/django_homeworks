from django.db import models
from django.urls import reverse
from django.utils import timezone

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

    def __str__(self):
        return f'{self.name}: {self.price:.3}'

    def get_absolute_url(self):
        return reverse('store_app:product', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name', 'price', 'create_date', 'modify_date', 'category',)
