from django.db import models
from django.urls import reverse


class Header(models.Model):
    title = models.CharField(max_length=250, default='Cool', verbose_name='Название')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Аватарка')
    slogan = models.TextField(blank=True, verbose_name='Слоган')
    work_hours = models.CharField(max_length=250, verbose_name='Часы работы')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    fon = models.CharField(max_length=250, verbose_name='Телефон')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Данные компании'
        verbose_name_plural = 'Данные компании'

class TopMenu(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

    def get_absolute_url(self):
        return reverse('view_topmenu', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'

class Doctor(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото доктора')
    specialization = models.ForeignKey('Specialization', on_delete=models.PROTECT, verbose_name='Специализация')

    def get_absolute_url(self):
        return  reverse('view_doctor', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

class Specialization(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Специализация')

    def get_absolute_url(self):
        return reverse('specialization', kwargs={'specialization_id':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = 'Специализации'
        ordering = ['title']


class Action(models.Model):
    title = models.CharField(max_length=250, verbose_name='Акции')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

class Discounts(models.Model):
    title=models.CharField(max_length=150, verbose_name='Название')
    content= models.TextField(verbose_name='Контент')

    def get_absolute_url(self):
        return reverse('discount', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

class Article(models.Model):
    title=models.CharField(max_length=150, verbose_name='Название')
    content= models.TextField(verbose_name='Контент')

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'






