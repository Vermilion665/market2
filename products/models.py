from django.db import models
from django.urls import reverse
from slugify import slugify
import os

# Create your models here.

def create_directory_path(instance, filename):
    '''Функция возвращает путь к директории, где должны храниться изображения'''
    filename = os.path.join('images/', instance.category.slug, instance.subcategory.slug)
    return filename
    #return f'images/{instance.category.slug}/{instance.subcategory.slug}'

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Описание категории')
    slug = models.SlugField(max_length=256, unique=True, verbose_name='URL-name', editable=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    
class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True,  verbose_name='Имя подкатегории')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', null=False, blank=False, related_name='categories')
    slug = models.SlugField(max_length=70, unique=True, verbose_name='URL-name', editable=False)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name',]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product-list', kwargs={'cat_slug':self.category.slug, 'subcat_slug': self.slug})


class Products(models.Model):
    name = models.CharField(max_length=128, verbose_name='Товар', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена товара')
    slug = models.SlugField(max_length=148, unique=True, verbose_name='URL-name', editable=False)
    is_available = models.BooleanField(default=True, verbose_name='Доступность')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата добавление товара')
    image = models.ImageField(upload_to=create_directory_path, verbose_name='Изображение товавра', null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория', editable=False, related_name='subcategory')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', editable=False, related_name='category')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-price']

    def get_absolute_url(self):
        '''Данная функция возвращает абсолютный URL для конкретного продукта.
        Она использует функцию reverse() из модуля django.urls для получения URL-адреса продукта.
        В аргументах функции reverse() передаются именованные параметры, которые используются для строительства URL-адреса.
        В данном случае, используются значения slug связанных категории, подкатегории и самого продукта.'''
        return reverse('products:product-detail', kwargs={
            'cat_slug': self.category.slug,
            'subcat_slug': self.subcategory.slug,
            'prod_slug': self.slug,
            }
        )    

    def __str__(self) -> str:
        '''Функция возвращает атрибут "name" объекта, на котором она вызывается, в виде строки.'''
        return self.name

    def save(self, *args, **kwargs):
        '''Функция сохраняет данные объекта модели Products в базу данных.
        Функция slugify() используется для преобразования строки в строку без пробелов и специальных символов,
        которая может быть использована в URL'''
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)
    