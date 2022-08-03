from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', AppleHome.as_view(), name="apple"),
    path('ipad/', ipad, name="ipad"),
    path('iphone/', iphone, name="iphone"),
    path('imac/', imac, name="imac"),
    path('add_page/', AddPage.as_view(), name="add_page"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>/', AppleCategory.as_view(), name="category"),
]
