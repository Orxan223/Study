from modeltranslation.translator import translator, TranslationOptions, register
from .models import *

@register(About)
class AboutTranslation(TranslationOptions):
    fields=('who_are_we', 'title')


@register(Service)
class ServiceTranslation(TranslationOptions):
    fields=('title', 'text')

@register(ForWorkPage)
class ForWorkPage(TranslationOptions):
    fields=('title', 'text')


@register(Feature)
class Feature(TranslationOptions):
    fields=('title', 'text')


@register(DetailsFeature)
class DetailsFeature(TranslationOptions):
    fields=('title', 'text')


