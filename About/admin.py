from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class AboutAdmin(TranslationAdmin):
    model=About


class ForWorkPageAdmin(TranslationAdmin):
    model=ForWorkPage

    

class ServiceAdmin(TranslationAdmin):
    model=Service


class FeatureAdmin(TranslationAdmin):
    model=Feature


class DetailsFeatureAdmin(TranslationAdmin):
    model=DetailsFeature




admin.site.register(About, AboutAdmin)
admin.site.register(ImageForAbout)
admin.site.register(ForWorkPage, ForWorkPageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(DetailsFeature, DetailsFeatureAdmin)