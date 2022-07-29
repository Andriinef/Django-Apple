from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


menu = [{'title': "Продукцiя APPLE", 'url_name': "apple"},
        {'title': "Додати статтю", 'url_name': "add_page"},
        {'title': "Зворотній зв'язок", 'url_name': "contact"},
        {'title': "Увійти", 'url_name': "login"},
        ]


# Create your views here.
def apple(request):
    posts = Apple.objects.all

    context = {"menu": menu,
               "posts": posts,
               "title": "Продукцiя APPLE",
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
    if request.method == 'POST':
        form = Add_Post_Fofm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Apple.objects.create(**form.cleaned_data)
                return redirect('apple')
            except:
                form.add_error(None, 'Помилка додавання посту')
    else:
        form = Add_Post_Fofm()
    return render(request, "apple/add_page.html", {'form': form, 'menu': menu, 'title': "Додати статтю"})


def contact(request):
    return HttpResponse("Зворотній зв'язок")


def login(request):
    return HttpResponse("Автоматизація")


def show_post(request, post_slug):
    post = get_object_or_404(Apple, slug=post_slug)

    context = {
        "post": post,
        "menu": menu,
        "title": post.title,
        "cat_selected": post.cat_id,
    }

    return render(request, 'apple/post.html', context=context)


def show_category(request, cat_id):
    posts = Apple.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {"menu": menu,
               "posts": posts,
               "title": "Категорії APPLE",
               "cat_selected": cat_id,
               }
    return render(request, "apple/apple.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")
