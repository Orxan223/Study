from django.urls import path
from .views import *

urlpatterns=[
    path('', apply_forms, name='apply'),
    path('how-to-apply', show_scheme, name='show_scheme')
]