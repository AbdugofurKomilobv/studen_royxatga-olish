
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls'),name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)