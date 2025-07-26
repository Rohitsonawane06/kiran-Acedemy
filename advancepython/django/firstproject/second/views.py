from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'profil.html')

def help(request):
    return render(request,'help.html')
