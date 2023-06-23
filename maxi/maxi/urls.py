from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views.generic import TemplateView
from gestion import urls as gestionurls
from api import urls as apiurls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(apiurls)),
    path('',include(gestionurls)),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)