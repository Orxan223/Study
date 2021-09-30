from django.core.files import storage
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.

class About(models.Model):
    who_are_we=models.CharField(max_length=50, blank=True, null=True)
    title=models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.who_are_we
    

class ImageForAbout(models.Model):
    img=models.ImageField(upload_to='about/', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=True, null=True)


class Service(models.Model):
    title=models.CharField(max_length=80, blank=False, null=False)
    text=models.TextField(blank=False, null=False)
    services_img=models.ImageField(upload_to='services/')

    def __str__(self) -> str:
        return self.title    


class ForWorkPage(models.Model):
    title=models.CharField(max_length=100, blank=True, null=True)
    text=models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return self.title


class Feature(models.Model):
    title=models.CharField(max_length=100, blank=True, null=True)
    text=models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return self.title

class DetailsFeature(models.Model):
    title=models.CharField(max_length=80, blank=True, null=True)
    text=models.TextField(blank=False, null=False)
    feature=models.ForeignKey(Feature, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.feature.title