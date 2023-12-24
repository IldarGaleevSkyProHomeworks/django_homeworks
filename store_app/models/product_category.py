from django.db import models
from utils.const import MF_NULL


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1024, verbose_name='описание', **MF_NULL)

    def __str__(self):
        return f'{self.name}: {self.description[:15]}' if self.description else self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
