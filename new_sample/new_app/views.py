from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def counter(request):
    # text = request.POST['text']
    # amount_of_words = len(text.split())
    # return render(request, 'counter.html', {'amount': amount_of_words})

    t=request.GET['text']
    n=int(t)
    sum=0
    while n>0:
        d=n%10
        sum=sum+d
        n=n//10
    return render(request,'counter.html',{'sod':sum})

    # Create your views here.
