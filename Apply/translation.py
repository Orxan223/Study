from modeltranslation.translator import translator, TranslationOptions, register
from .models import *


@register(EduDegree)
class EduDegreeTranslation(TranslationOptions):
    fields=('degree',)



@register(HowToApply)
class HowToApplyTranslation(TranslationOptions):
    fields=('title', 'text')
