from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import about
from .models import slider
from .models import client

def home(request):
    aboutdata = about.objects.all()[1]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    context={
        'about':aboutdata,
        'slider':sliderdata,
        'client':clientdata
    }
    return render(request,'index.html',context)

def aboutus(request):
    return HttpResponse('This is about page')


