from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic data is inserted')

def insert_webpage(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    url=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('webpage data is inserted')


def insert_accessrecords(request):
    n=input('enter name')
    a=input('enter auther')
    d=input('enter date')
    WO=Webpage.objects.get_or_create(name=n)[0]
    WO.save()
    AO=AccessRecords.objects.get_or_create(Webpage=WO,auther=a,date=d)[0]
    AO.save()
    return HttpResponse('accessrecords data is inserted')
    

    
   


