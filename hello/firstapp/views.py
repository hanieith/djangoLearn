from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person

def index(request):
    people = Person.objects.all()
    return render(request, "firstapp/index.html", {"people": people})

def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")