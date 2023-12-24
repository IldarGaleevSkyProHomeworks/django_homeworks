from django.db import models

from utils.const import MF_NULL


class WordFilter(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    regular_expression = models.CharField(max_length=255, verbose_name='регулярное выражение')
    comment = models.CharField(max_length=255, verbose_name='комментарий', **MF_NULL)
    is_enable = models.BooleanField(default=True, verbose_name='активно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'фильтр слов'
        verbose_name_plural = 'фильтры слов'
