from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields=('name',)


@register(News)
class NewsTranslation(TranslationOptions):
    fields=('title', 'text',)

    