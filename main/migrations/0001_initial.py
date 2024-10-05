# Generated by Django 5.1.1 on 2024-10-05 06:02

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('birth_date', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol'), ('Boshqa', 'Boshqa')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField(choices=[('Toshkent', 'Toshkent'), ('Andijon', 'Andijon'), ('Samarqand', 'Samarqand'), ('Buxoro', 'Buxoro')], max_length=50)),
                ('city_or_district', models.CharField(choices=[('Toshkent shahar', 'Toshkent shahar'), ('Andijon shahar', 'Andijon shahar'), ('Samarqand shahar', 'Samarqand shahar')], max_length=50)),
                ('profile_image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=90, scale=None, size=[100, 100], upload_to='profiles/')),
            ],
        ),
    ]
