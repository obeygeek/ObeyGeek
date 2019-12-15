# this file make by @DonzayStone .
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("hello")

def about(request):
    return HttpResponse("hello about")

def blog(request):
    return HttpResponse("hello blog")

def contact(request):
    return HttpResponse("hello contact")
