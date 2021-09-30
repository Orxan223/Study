from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class SliderAdmin(TranslationAdmin):
    model=Slider

admin.site.register(Slider, SliderAdmin)
admin.site.register(Logo)
# admin.site.register(Languages)