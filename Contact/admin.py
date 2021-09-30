from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class ContactInformationAdmin(TranslationAdmin):
    model=ContactInformation


class GeneralInformationAdmin(TranslationAdmin):
    model=GeneralInformation



admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(ContactImage)
admin.site.register(Contact)
admin.site.register(GeneralInformation, GeneralInformationAdmin)
admin.site.register(SocialProfile)
admin.site.register(Whatsapp)


 