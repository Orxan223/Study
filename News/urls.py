from django.urls.conf import path
from .views import *

urlpatterns=[
    path('', get_news, name='get_news'),
    path('news-detail/<int:id>', show_news_details, name='news_detail')
]