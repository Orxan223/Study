from django.shortcuts import render
from .models import *
# Create your views here.


def get_universities(request):
    uni_private=University.objects.filter(uni_choices='Özel')
    uni_state=University.objects.filter(uni_choices='Devlet')
    context={
        'uni_private':uni_private,
        'uni_state':uni_state
    }

    return render(request, 'universiteler.html', context)
