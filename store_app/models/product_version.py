from django.db import models

from store_app.models import Product


class ProductVersion(models.Model):
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.IntegerField(verbose_name='номер версии', default=0)
    is_latest = models.BooleanField(verbose_name='последняя версия')

    def __str__(self):
        return f'{self.version_name} ({self.version_number}){(" - active" if self.is_latest else "")}'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продукта'
