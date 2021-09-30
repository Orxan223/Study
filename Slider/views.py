from django.shortcuts import render
from .models import *
from Contact.models import SocialProfile
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
# Create your views here.


def show_base(request):
    slider=Slider.objects.all()
    logo=Logo.objects.first()
    social=SocialProfile.objects.first()
    print(dir(request.resolver_match.url_name))
    context={
        'slider':slider,
        
    
    }

    return render(request, 'footer.html', context)

def logo(request):
    logo=Logo.objects.first()
    social=SocialProfile.objects.first()
    logo=logo.image.url
    twitter=social.twitter
    print(twitter)
    if twitter is None:
        twitter="None"

    return JsonResponse({
        'logo':logo,
        'facebook':social.facebook,
        'instagram':social.instagram,
        'twitter':twitter,
        'youtube': social.youtube
        })


