# Generated by Django 3.2.7 on 2021-09-29 07:14

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='img_az',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to='slider/'),
        ),
        migrations.AddField(
            model_name='slider',
            name='img_en',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to='slider/'),
        ),
        migrations.AddField(
            model_name='slider',
            name='img_ru',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to='slider/'),
        ),
    ]
