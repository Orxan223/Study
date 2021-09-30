from django.shortcuts import render
from .models import *
# Create your views here.


def get_info(request):
    about=About.objects.all()[:4]
    image=ImageForAbout.objects.first()
    
    context={
        'about':about,
        'image':image
        
    }

    return render(request, 'hakkimizda.html', context )


def show_services(request):
    service=Service.objects.all()

    context={
        'service':service
    }

    return render(request, 'hizmetlerimiz.html', context )

def show_features(request):
    features=Feature.objects.all()
    # about=About.objects.first()
    work_page=ForWorkPage.objects.all()[:4]

    context={
        'features':features,
        'work_page':work_page
    }

    return render(request, 'turkiyede-calisma.html', context)

def show_details(request,id):
    feature=Feature.objects.get(id=id)
    details=DetailsFeature.objects.filter(feature=feature)

    context={
        'feature':feature,
        'details':details
    }

    return render(request, 'oturmaizni.html', context)
