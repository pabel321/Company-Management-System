from django.http import HttpResponse
from django.shortcuts import render
from . import views

def employee(request):
    return HttpResponse("This is our Employee Page")
def profile(request):
    return render(request,'employee/profile.html')