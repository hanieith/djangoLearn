from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    return render(request, "firstapp/index.html")

def about(request, productid=1):
    return render(request, "firstapp/about.html")

