from modeltranslation.translator import translator, TranslationOptions, register
from .models import *


@register(ContactInformation)
class ContactInformationTranslation(TranslationOptions):
    fields=('title', 'text',)


@register(GeneralInformation)
class GeneralInformationTranslation(TranslationOptions):
    fields=('country','location',)


    