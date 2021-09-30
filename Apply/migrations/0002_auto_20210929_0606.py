# Generated by Django 3.2.7 on 2021-09-29 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edudegree',
            name='degree_az',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='edudegree',
            name='degree_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='edudegree',
            name='degree_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='howtoapply',
            name='text_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='howtoapply',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='howtoapply',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='howtoapply',
            name='title_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='howtoapply',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='howtoapply',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
