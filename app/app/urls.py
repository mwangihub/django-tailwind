
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # noqa

urlpatterns = [
    path('', include("src.urls")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
