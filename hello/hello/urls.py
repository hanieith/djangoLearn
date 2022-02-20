from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
]
