from django.urls import path
from .views import *

urlpatterns=[
    path('aboutus/', get_info, name='get_info'),
    path('services', show_services, name='show_services'),
    path('features', show_features, name='show_features'),
    path('features-detail/<int:id>', show_details, name='show_details'),
]