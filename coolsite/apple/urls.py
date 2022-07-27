from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', apple, name="apple"),
    path('ipad/', ipad, name="ipad"),
    path('iphone/', iphone, name="iphone"),
    path('imac/', imac, name="imac"),
    path('add_page/', add_page, name="add_page"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('post/<int:post_id>/', show_post, name="post"),
    path('category/<int:cat_id>/', show_category, name="category"),
]
