from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse(f"Коректное имя {name}")
    return render(request, "firstapp/index.html", {"form": userform})

