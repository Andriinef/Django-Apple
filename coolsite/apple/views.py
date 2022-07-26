from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["Продукция APPLE", "Добавить статью", "Обратная связь", "Войти"]


# Create your views here.
def apple(request):
    return render(request, "apple/apple.html", {"menu": menu, "title": "Продукция APPLE"})


def ipad(request):
    posts = Apple.objects.filter(pk__lte=5)
    return render(request, "apple/ipad.html", {"menu": menu, "posts": posts, "title": "iPad APPLE"})


def iphone(request):
    return render(request, "apple/iphone.html", {"menu": menu, "title": "iPhone APPLE"})


def categories(request, cat_slug):
    if request.GET:
        print(request.GET)
    elif request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat_slug}</p>")


def archive(request, year):
    if int(year) < 999:
        raise Http404()
    elif int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архивы по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
