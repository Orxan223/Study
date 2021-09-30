from typing import Text
from django.core.files import storage
from django.db import models
from university.models import *
from django.utils.translation import ugettext as _
# Create your models here.

Gender=[
    ('Erkek', _('Erkek')),
    ('Kadın', _('Kadın'))
]

class Country(models.Model):
    name=models.CharField(max_length=120, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

class EduDegree(models.Model):
    degree=models.CharField(max_length=150, blank=False, null=False)

    def __str__(self) -> str:
        return self.degree

class EduLanguage(models.Model):
    lang=models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.lang

class Currency(models.Model):
    currency=models.CharField(max_length=5, blank=False, null=False)

    def __str__(self) -> str:
        return self.currency



def form_directory_path(instance, filename):
    
    location="applyform/{}_{}/".format(instance.name, instance.surname)
    return location + filename





class StudentApply(models.Model):
    name=models.CharField(max_length=80, blank=False, null=False)
    surname=models.CharField(max_length=80, blank=False, null=False)
    country=models.ForeignKey(Country, on_delete=models.CASCADE , blank=False, null=False)
    born_date=models.DateField(blank=False, null=False)
    # faculty=models.CharField(max_length=120, blank=False, null=False)
    phone=models.CharField(max_length=120, blank=False, null=False)
    email=models.EmailField(max_length=100, blank=False, null=False)
    university=models.ForeignKey(University, on_delete=models.CASCADE, blank=False, null=False)
    program=models.CharField(max_length=150, blank=False, null=False)
    edu_degree=models.ForeignKey(EduDegree, on_delete=models.CASCADE)
    edu_lang=models.ForeignKey(EduLanguage, on_delete=models.CASCADE)
    edu_currency=models.ForeignKey(Currency, on_delete=models.CASCADE)
    budget=models.IntegerField(blank=False, null=False )
    diploma=models.FileField(upload_to=form_directory_path, storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    note=models.FileField(upload_to=form_directory_path, storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    passport=models.FileField(upload_to=form_directory_path, storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    photo=models.ImageField(upload_to=form_directory_path, storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    gender=models.CharField(max_length=5, choices=Gender, default='Cinsiyettiniz', blank=False, null=False)
    message=models.TextField(blank=False, null=False)

    


class HowToApply(models.Model):
    title=models.CharField(max_length=100, blank=False, null=True)
    text=models.TextField(blank=False, null=False)


class ImgForApply(models.Model):
    img=models.ImageField(upload_to='simpleforpages/', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=True, null=True)






