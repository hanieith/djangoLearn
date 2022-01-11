from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    # return render(request, 'firstapp\home.html')
    data ={'header': 'Передача параметров в шаблон джанго',
            'message': 'загружен шаблон templates/firstapp/index_app1.html'}
    return render(request, 'firstapp/index_app1.html', context=data)

def about(request):
    return HttpResponse("<h2>0 сайте</h2>")

def contact(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')

def products(request, productid=1):
    category = request.GET.get("cat", "")
    output = f"<h2>Продукт № {productid} Категория: {category}</h2>"
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = f"<h2>Пользователь</h2><h3>id:{id}</h3><h3>name:{name}</h3>"
    return HttpResponse(output)