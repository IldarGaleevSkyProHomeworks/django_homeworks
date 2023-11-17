
from django.db import models
from django.utils import timezone

# Create your models here.

nullable = {
    'null': True,
    'blank': True
}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1024, verbose_name='описание', **nullable)

    def __str__(self):
        return f'{self.name}: {self.description[:15]}' if self.description else self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1024, verbose_name='описание', **nullable)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена', default=0.0)
    create_date = models.DateTimeField(verbose_name='дата создания', default=timezone.now)
    modify_date = models.DateTimeField(verbose_name='дата изменения', default=timezone.now)
    preview_image = models.ImageField(upload_to='product_preview_images/', verbose_name='изображение', **nullable)

    def __str__(self):
        return f'{self.name}: {self.price:.3}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name', 'price', 'create_date', 'modify_date', 'category',)
