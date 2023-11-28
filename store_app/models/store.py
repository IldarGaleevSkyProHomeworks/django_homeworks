from django.db import models
from django.urls import reverse
from django.utils import timezone

from .const import NULLABLE
from store_app.utils.HashStorage import product_preview_images, HashStorage


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1024, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.description[:15]}' if self.description else self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1024, verbose_name='описание', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена', default=0.0)
    create_date = models.DateTimeField(verbose_name='дата создания', default=timezone.now)
    modify_date = models.DateTimeField(verbose_name='дата изменения', default=timezone.now)
    preview_image = models.ImageField(upload_to=product_preview_images, storage=HashStorage(),
                                      verbose_name='изображение', **NULLABLE)  # 'product_preview_images/'

    def __str__(self):
        return f'{self.name}: {self.price:.3}'

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name', 'price', 'create_date', 'modify_date', 'category',)


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя отделения')
    phones = models.CharField(max_length=255, verbose_name='телефоны')
    address = models.CharField(max_length=255, verbose_name='адрес')
    order = models.IntegerField(verbose_name='порядок отображения', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('order',)
