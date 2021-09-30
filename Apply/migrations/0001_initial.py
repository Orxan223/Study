# Generated by Django 3.2.7 on 2021-09-28 18:50

import Apply.models
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='EduDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EduLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='HowToApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImgForApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to='simpleforpages/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('born_date', models.DateField()),
                ('phone', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=100)),
                ('program', models.CharField(max_length=150)),
                ('budget', models.IntegerField()),
                ('diploma', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to=Apply.models.form_directory_path)),
                ('note', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to=Apply.models.form_directory_path)),
                ('passport', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to=Apply.models.form_directory_path)),
                ('photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/zaur/Study-pro/Study/media'), upload_to=Apply.models.form_directory_path)),
                ('gender', models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], default='Cinsiyettiniz', max_length=5)),
                ('message', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apply.country')),
                ('edu_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apply.currency')),
                ('edu_degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apply.edudegree')),
                ('edu_lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apply.edulanguage')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.university')),
            ],
        ),
    ]
