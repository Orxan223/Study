from django.core.exceptions import ValidationError
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.

class ContactInformation(models.Model):
    title=models.CharField(max_length=80, blank=False, null=False)
    text=models.TextField(blank=False, null=False)


class ContactImage(models.Model):
    img=models.ImageField(upload_to='contact/', storage=FileSystemStorage(settings.MEDIA_ROOT))


class Contact(models.Model):
    fullname=models.CharField(max_length=80, blank=False, null=False)
    email=models.EmailField(max_length=80, blank=False, null=True)
    phone=models.CharField(max_length=120, blank=False, null=False)    
    message=models.TextField(blank=False, null=False)


class GeneralInformation(models.Model):
    country=models.CharField(max_length=30, blank=False, null=False)
    location=models.CharField(max_length=120, blank=False, null=False)
    phone=models.CharField(max_length=20, blank=False, null=False)
    additionally_info=models.CharField(max_length=20, blank=True, null=True)

class Whatsapp(models.Model):
    whatsapp=models.CharField(max_length=20, blank=False, null=False)
    email=models.EmailField(max_length=80, blank=False, null=False)


class SocialProfile(models.Model):
    facebook=models.URLField(blank=False, null=False)
    twitter=models.URLField(blank=True, null=True)
    instagram=models.URLField(blank=False, null=False)
    youtube=models.URLField(blank=False, null=False)

    def save(self, *args,**kwargs):
        if not self.pk and SocialProfile.objects.exists():
            return False
        return super(SocialProfile, self).save(*args, **kwargs)    


