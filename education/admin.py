from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class EducationAdmin(TranslationAdmin):
    model=Education

class GuestAdmin(TranslationAdmin):
    model=Guest 

admin.site.register(Education, EducationAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(ImagesForGuest)