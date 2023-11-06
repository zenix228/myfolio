from django.contrib import admin
from django.urls import path, include
from apps.post.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('post/', post, name='post'),
    path('post_detail/<pk>/', post_detail, name='post_detail'),
    path('create/', create, name='create'),
]
