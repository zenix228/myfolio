from django.contrib import admin
from django.urls import path, include
from apps.post.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('', home, name='home'),
    path('post/', include('apps.post.urls')),
    path('account/', include('apps.user.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )