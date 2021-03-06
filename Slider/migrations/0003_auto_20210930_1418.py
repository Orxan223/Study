# Generated by Django 3.1.6 on 2021-09-30 10:18

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slider', '0002_auto_20210929_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to='slider/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img_az',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to='slider/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img_en',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to='slider/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img_ru',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to='slider/'),
        ),
    ]
