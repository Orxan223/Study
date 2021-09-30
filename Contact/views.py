from django.shortcuts import render
from .models import *
# Create your views here.

def to_fill_for_contact(request):
    general_info=GeneralInformation.objects.all()
    social=SocialProfile.objects.first()
    whatsapp=Whatsapp.objects.first()
    if request.method == "POST":
        contact=Contact.objects.create(
            fullname=request.POST.get('fullname'),
            email=request.POST.get('mail'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
    
    

    context={
        'general':general_info,
        'whatsapp':whatsapp,
        'social':social
    }    

    return render(request, 'iletisim.html', context)    
