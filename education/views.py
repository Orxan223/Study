from django.shortcuts import render
from .models import *
# Create your views here.

def get_edu_info(request):
    edu=Education.objects.all()
    
    
    context={
        'edu':edu,
    }

    return render(request, 'turkiyede-egitim.html', context)


def show_guest(request):
    guests=Guest.objects.all()
    image=ImagesForGuest.objects.first()

    context={
        'guest':guests,
        'image':image
    }

    return render(request, 'konaklama.html', context)    