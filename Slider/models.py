from django.core.files import storage
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import  settings
# Create your models here.


class Slider(models.Model):
    img=models.ImageField(upload_to='slider/', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    link=models.URLField(blank=False, null=False)


# class Languages(models.Model):
#     lang=models.CharField(max_length=2  ,blank=False, null=False)
#     image=models.ImageField(upload_to='langs', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)


class Logo(models.Model):
    image=models.ImageField(upload_to='logo/', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    # is_active=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk and Logo.objects.exists():
            return False
        super(Logo, self).save(*args, **kwargs)    

