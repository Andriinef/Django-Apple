from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class AppleHome(DataMixin, ListView):
    model = Apple
    template_name = "apple/apple.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Apple.objects.filter(is_published=True)


# def apple(request):
#     posts = Apple.objects.all
#
#     context = {"menu": menu,
#                "posts": posts,
#                "title": "Продукцiя APPLE",
#                "cat_selected": 0,
#                }
#     return render(request, "apple/apple.html", context=context)


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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = Add_Post_Fofm
    template_name = "apple/add_page.html"
    success_url = reverse_lazy("apple")
    login_url = reverse_lazy("apple")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавлення сторінка")
        return dict(list(context.items()) + list(c_def.items()))


# def add_page(request):
#     if request.method == 'POST':
#         form = Add_Post_Fofm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('apple')
#     else:
#         form = Add_Post_Fofm()
#     return render(request, "apple/add_page.html", {'form': form, 'menu': menu, 'title': "Додати статтю"})


def contact(request):
    return HttpResponse("Зворотній зв'язок")


def login(request):
    return HttpResponse("Автоматизація")


class ShowPost(DataMixin, DetailView):
    model = Apple
    template_name = "apple/post.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"])
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(Apple, slug=post_slug)
#
#     context = {
#         "post": post,
#         "menu": menu,
#         "title": post.title,
#         "cat_selected": post.cat_id,
#     }
#
#     return render(request, 'apple/post.html', context=context)


class AppleCategory(DataMixin, ListView):
    model = Apple
    template_name = "apple/apple.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        return Apple.objects.filter(cat__slug=self.kwargs["cat_slug"], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категорія - " + str(context["posts"][0].cat),
                                      cat_selected=context["posts"][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_id):
#     posts = Apple.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404
#
#     context = {"menu": menu,
#                "posts": posts,
#                "title": "Категорії APPLE",
#                "cat_selected": cat_id,
#                }
#     return render(request, "apple/apple.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'apple/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Реєстрація')
        return dict(list(context.items()) + list(c_def.items()))
