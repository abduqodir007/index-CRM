# Generated by Django 5.1.1 on 2024-10-05 11:15

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
            ],
            options={
                'verbose_name': 'project category',
                'verbose_name_plural': 'project categories',
                'db_table': 'project_category',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
            ],
            options={
                'verbose_name': 'product tag',
                'verbose_name_plural': 'product tags',
                'db_table': 'product_tag',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('slug', models.SlugField(max_length=256, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('small_image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[50, 50], upload_to='products/%Y/%m', verbose_name='image small')),
                ('main_image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[545, 621], upload_to='products/%Y/%m', verbose_name='image main')),
                ('main_image1', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[545, 621], upload_to='products/%Y/%m', verbose_name='image main')),
                ('main_image2', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[545, 621], upload_to='products/%Y/%m', verbose_name='image main')),
                ('main_image3', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[545, 621], upload_to='products/%Y/%m', verbose_name='image main')),
                ('main_image4', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[545, 621], upload_to='products/%Y/%m', verbose_name='image main')),
                ('is_top', models.BooleanField(default=False, verbose_name='project is top')),
                ('published_date', models.DateField(auto_now_add=True, verbose_name='published date')),
                ('price', models.CharField(max_length=256, verbose_name='price')),
                ('brand', models.CharField(max_length=256, verbose_name='brand')),
                ('Product_code', models.CharField(max_length=256, verbose_name='Product code')),
                ('Product_qount', models.CharField(max_length=100, verbose_name='product qount')),
                ('categories', models.ManyToManyField(related_name='products', to='main.productcategory', verbose_name='categories')),
                ('tags', models.ManyToManyField(related_name='products', to='main.producttag', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
    ]
