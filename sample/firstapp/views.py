from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name="Pallavi"
    return render(request,"index.html",{'name':name})


def about(request):
    return render(request,"about.html")

def welcome(request):
    name1 = "django"
    return render(request, "welcome.html",{'name':name1})

# Create your views here.
