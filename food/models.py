from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Filter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фильтра')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='filters', verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'

    def __str__(self):
        return f"{self.category.name}: {self.name}"


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='food_images/', verbose_name='Картинка', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    filters = models.ManyToManyField(Filter, related_name='foods', verbose_name='Фильтры')

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return _("Нет изображения")

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'

    def __str__(self):
        return self.name
