from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(60)(AppleHome.as_view()), name="apple"),
    path('ipad/', ipad, name="ipad"),
    path('iphone/', iphone, name="iphone"),
    path('imac/', imac, name="imac"),
    path('add_page/', AddPage.as_view(), name="add_page"),
    path('contact/', ContactFormView.as_view(), name="contact"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>/', AppleCategory.as_view(), name="category"),
]

