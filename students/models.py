from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=80, blank=False, null=False)
    surname=models.CharField(max_length=100, blank=False, null=False)
    acceptance_form=models.ImageField(upload_to='student/', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)

