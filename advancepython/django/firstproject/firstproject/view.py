from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hellow")
    return render(request,'home.html')

def about(request):
    return HttpResponse("<h1> About ")

def contact(request):
    return HttpResponse("h1 style='")

def help(request):
    return HttpResponse("This is the Help page")