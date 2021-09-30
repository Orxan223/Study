from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(Slider)
class SliderTranslation(TranslationOptions):
    fields=('img',)

