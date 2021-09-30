from django.urls.conf import path
from .views import *

urlpatterns=[
    path('', show_base, name='base'),
    path('logo', logo, name='logo')
    
]