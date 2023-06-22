from django.urls import path
from .views import autos, detalle_auto, servicios, detalle_servicio

# define the urls
urlpatterns = [
    path('autos/', autos),
    path('autos/<int:pk>/', detalle_auto),
    path('servicios/', servicios),
    path('servicio/<int:pk>/', detalle_servicio),
]