# Generated by Django 4.2.4 on 2023-09-12 08:29

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_category_slug_alter_products_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=70, unique=True, verbose_name='URL-имя'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.create_directory_path, verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Доступность товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(editable=False, max_length=148, unique=True, verbose_name='URL-имя'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(editable=False, max_length=70, unique=True, verbose_name='URL-имя'),
        ),
    ]
