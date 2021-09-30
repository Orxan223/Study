# Generated by Django 3.2.7 on 2021-09-29 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='text_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_az',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
    ]
