from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', apple, name="apple"),
    path('ipad/', ipad, name="ipad"),
    path('iphone/', iphone, name="about"),
]
