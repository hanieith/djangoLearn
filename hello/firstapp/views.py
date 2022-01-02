from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Глaвнaя</h2>")

def about(request):
    return HttpResponse("<h2>0 сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid=1):
    output = f"<h2>Продукт № {productid}</h2>"
    return HttpResponse(output)

def users(request, id, name):
    output = f"<h2>Пользователь</h2><h3>id:{id}</h3><h3>name:{name}</h3>"
    return HttpResponse(output)