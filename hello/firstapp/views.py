from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = f"<h2>Пользователь</h2><h3>Имя - {name}, Возраст - {age}</h3>"
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})

def about(request, productid=1):
    return render(request, "firstapp/about.html")

