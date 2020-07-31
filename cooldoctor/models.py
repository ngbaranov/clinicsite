from django.db import models


class Header(models.Model):
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Аватарка')
    slogan = models.TextField(blank=True, verbose_name='Слоган')
    work_hours = models.CharField(max_length=250, verbose_name='Часы работы')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    fon = models.CharField(max_length=250, verbose_name='Телефон')

    def __str__(self):
        return 'Классный доктор'

    class Meta:
        verbose_name = 'Данные компании'
        verbose_name_plural = 'Данные компании'

