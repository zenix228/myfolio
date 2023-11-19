from django.urls import path, include
from apps.user import views
from django.contrib.auth import views as auth_views


urlpatterns = [
#    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
