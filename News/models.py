from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=60, blank=False, null=False)

    def __str__(self) -> str:
        return self.name



class News(models.Model):
    title=models.CharField(verbose_name=_('title'),max_length=150, blank=False, null=False)
    text=models.TextField(blank=False, null=False)
    news_img=models.ImageField(upload_to='news/', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    views=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    