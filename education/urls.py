from django.urls.conf import path
from .views import *

urlpatterns=[
    path('', get_edu_info, name='get_edu_info'),
    path('guests', show_guest, name='show_guest')
]