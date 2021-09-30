from django.shortcuts import render
from .models import *
# Create your views here.

def show_students(request):
    student=Student.objects.all()

    context={
        'student':student
    }

    return render(request, 'kabuller.html', context)