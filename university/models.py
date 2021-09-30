from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.translation import ugettext as _
# Create your models here.

UNI_CHOICES=[
    ('Özel',_('Özel')),
    ('Devlet', _('Devlet'))
]

class University(models.Model):
    uni_name=models.CharField(max_length=80, blank=False, null=False)
    uni_img=models.ImageField(upload_to='university/', storage=FileSystemStorage(location=settings.MEDIA_ROOT), blank=False, null=False)
    uni_choices=models.CharField(choices=UNI_CHOICES, max_length=6)

    def __str__(self) -> str:
        return self.uni_name
    