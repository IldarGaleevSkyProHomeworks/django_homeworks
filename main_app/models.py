from django.db import models


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
