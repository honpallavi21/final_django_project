from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello,Welcome in django,This is my 1st app")
# Create your views here.
