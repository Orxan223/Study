from django.urls.conf import path
from .views import *

urlpatterns=[
    path('', show_students, name='show_students'),
]