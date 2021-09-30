from django.core.files import storage
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Education(models.Model):
    title=models.CharField(max_length=80, blank=False, null=False)
    text=models.TextField(blank=False, null=False)
    img=models.ImageField(upload_to='education/', storage=FileSystemStorage(settings.MEDIA_ROOT), blank=True, null=True)  
    

class Guest(models.Model):
    title=models.CharField(max_length=80, blank=False, null=False)
    text=models.TextField(blank=False, null=False)

class ImagesForGuest(models.Model):
    img=models.ImageField(upload_to='guests/', storage=FileSystemStorage(settings.MEDIA_ROOT), blank=False, null=False)



@receiver(post_save, sender=Education)
def id_add_to_title(sender, created, instance, *args, **kwargs):
   if created is True:
       count=sender.objects.all().count()
       instance.title='{}'.format(count) + " - " + instance.title
       instance.save()