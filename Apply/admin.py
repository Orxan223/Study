from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class EduDegreeAdmin(TranslationAdmin):
    model=EduDegree




class HowToApplyAdmin(TranslationAdmin):
    model=HowToApply        




admin.site.register(Country)
admin.site.register(EduDegree, EduDegreeAdmin)
admin.site.register(EduLanguage)
admin.site.register(Currency)
admin.site.register(StudentApply)
admin.site.register(HowToApply, HowToApplyAdmin)
admin.site.register(ImgForApply)
