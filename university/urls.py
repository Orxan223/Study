from django.urls import path
from .views import *


urlpatterns=[
    path('', get_universities, name='get_university')
]