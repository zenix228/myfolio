from django.contrib import admin
from django.urls import path, include
from apps.post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('apps.api.urls')),
    path('', home, name='home'),
    path('post/', include('apps.post.urls'))
]
