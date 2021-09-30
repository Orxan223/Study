from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Education)
class EducationTranslator(TranslationOptions):
    fields=('title', 'text',)


@register(Guest)
class GuestTranslator(TranslationOptions):
    fields=('title', 'text',)


