from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from university.models import University
# Create your views here.

def show_scheme(request):
    scheme=HowToApply.objects.all()
    img=ImgForApply.objects.first()
    context={
        'scheme':scheme,
        'img':img
    }

    return render(request, 'nasil-basvurulur.html', context)



def apply_forms(request):
    country=Country.objects.all()
    uni=University.objects.all()
    degree=EduDegree.objects.all()
    lang=EduLanguage.objects.all()
    currency=Currency.objects.all()

    f=ApplyForms(request.POST)
    print(request.FILES)

    if request.method == "POST":
        
        form=StudentApply.objects.create(
            name=request.POST.get('name'),
            surname=request.POST.get('surname'),
            country= Country.objects.get(id=int(request.POST.get('country'))),
            born_date=request.POST.get('born_date'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            university=University.objects.get(id=int(request.POST.get('uni'))), 
            program=request.POST.get('program'),
            edu_degree=EduDegree.objects.get(id=int(request.POST.get('edu_degree'))),
            edu_lang=EduLanguage.objects.get(id=int(request.POST.get('edu_lang'))),
            edu_currency=Currency.objects.get(id=int(request.POST.get('edu_currency'))),
            budget=request.POST.get('budget'),
            diploma=request.FILES.get('diploma'),
            passport=request.FILES.get('passport'),
            note=request.FILES.get('note'),
            photo=request.FILES.get('photo'),
            gender=request.POST.get('gender'),
            message=request.POST.get('message')
        )
        form.save()

   
    context={
        'ok':'ok',
        'country':country,
        'uni':uni,
        'degree':degree,
        'lang':lang,
        'currency':currency,
        'f':f
    }
    
    return render(request, 'basvuru-formu.html', context)
