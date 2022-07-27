from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "Продукция APPLE", 'url_name': "apple"},
        {'title': "Добавить статью", 'url_name': "add_page"},
        {'title': "Обратная связь", 'url_name': "contact"},
        {'title': "Войти", 'url_name': "login"},
        ]


# Create your views here.
def apple(request):
    posts = Apple.objects.filter(pk__lte=10)
    cats = Category.objects.all()

    context = {"menu": menu,
               "posts": posts,
               "cats": cats,
               "title": "Продукция APPLE",
               "cat_selected": 0,
               }
    return render(request, "apple/apple.html", context=context)


def ipad(request):
    context = {"menu": menu,
               "title": "iPad APPLE"
               }
    return render(request, "apple/ipad.html", context=context)


def iphone(request):
    context = {"menu": menu,
               "title": "iPhone APPLE"
               }
    return render(request, "apple/iphone.html", context=context)


def imac(request):
    context = {"menu": menu,
               "title": "iMac APPLE"
               }
    return render(request, "apple/imac.html", context=context)


def add_page(request):
    return HttpResponse("Добавить статью")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Автоматизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Apple.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {"menu": menu,
               "posts": posts,
               "cats": cats,
               "title": "Категории APPLE",
               "cat_selected": cat_id,
               }
    return render(request, "apple/apple.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
