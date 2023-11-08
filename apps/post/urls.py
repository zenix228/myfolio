from django.contrib import admin
from django.urls import path, include
from apps.post.views import *

urlpatterns = [
    path('', post, name='post'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('create/', create, name='create'),
    path('about/', about, name='about')
]