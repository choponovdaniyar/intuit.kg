from django.contrib import admin
from django.urls import path, include

from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls", namespace="main")),
    path('news/', include("news.urls", namespace='news')),
    path('', include("faculty.urls", namespace='faculty'))
]  
  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
