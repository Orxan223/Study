# Generated by Django 3.1.6 on 2021-09-30 10:18

import Apply.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0002_auto_20210929_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='edudegree',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='edulanguage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='howtoapply',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='imgforapply',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='imgforapply',
            name='img',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to='simpleforpages/'),
        ),
        migrations.AlterField(
            model_name='studentapply',
            name='diploma',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to=Apply.models.form_directory_path),
        ),
        migrations.AlterField(
            model_name='studentapply',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentapply',
            name='note',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to=Apply.models.form_directory_path),
        ),
        migrations.AlterField(
            model_name='studentapply',
            name='passport',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to=Apply.models.form_directory_path),
        ),
        migrations.AlterField(
            model_name='studentapply',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\USER\\Desktop\\studyy\\media'), upload_to=Apply.models.form_directory_path),
        ),
    ]
