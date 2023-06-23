from django.contrib import admin
from django.urls import path, include
from gestion import urls as gestionurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(gestionurls)),
    ]