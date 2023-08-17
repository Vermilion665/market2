from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Описание категории')
    slug = models.SlugField(max_length=70, unique=True, verbose_name='URL-name')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name

    def get_url(self):
        return reverse('category_detail', args=[self.slug])

    
class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True,  verbose_name='Имя подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name',]


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Товар', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена товара')
    slug = models.SlugField(max_length=148, unique=True, verbose_name='URL-name')
    is_available = models.BooleanField(default=True, verbose_name='Доступность')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата добавление товара')
    product_image = models.ImageField(upload_to='images/', verbose_name='Изображение товавра')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-price']

    def __str__(self) -> str:
        return self.name
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
