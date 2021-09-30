from .models import *
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class NewsAdmin(TranslationAdmin):
    model=News

class CategoryAdmin(TranslationAdmin):
    model=Category    

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)