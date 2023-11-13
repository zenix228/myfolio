from django.urls import path, include
from apps.user import views
from django.contrib.auth.views import *


urlpatterns = [
#    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login')
]
