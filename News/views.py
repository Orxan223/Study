from django.shortcuts import render
from .models import *
from datetime import date
# Create your views here.


def get_news(request):
    today=date.today()
    news=News.objects.all()
    news_for_today=News.objects.filter(timestamp__day=today.day)

    context={
        'news':news,
        'news_for_today':news_for_today
    }

    return render(request, 'home-news.html', context)


def show_news_details(request, id):
    news_detail=News.objects.get(id=id)
    today=date.today()
    mysessionlist=[]
    mysessionlist.append(request.session.session_key)
    daily=News.objects.filter(timestamp__day=today.day)
    if news_detail is not None:
        for x in mysessionlist:
            if x != request.session.session_key:
                news_detail.views+=1
                news_detail.save()

    context={
        'news_detail':news_detail,
        'daily':daily

    }

    return render(request, 'news.html', context)
