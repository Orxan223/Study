# Generated by Django 3.2.7 on 2021-09-28 18:50

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80, null=True)),
                ('phone', models.CharField(max_length=120)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(storage=django.core.files.storage.FileSystemStorage('/home/zaur/Study-pro/Study/media'), upload_to='contact/')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=20)),
                ('additionally_info', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField()),
                ('youtube', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Whatsapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=80)),
            ],
        ),
    ]
