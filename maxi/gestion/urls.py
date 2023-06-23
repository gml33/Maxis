from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_servicios, name=''),
    path('register',views.register, name='register'),
    path('my-login',views.my_login, name='my-login'),
    path('user-logout',views.user_logout, name='user-logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    #------------------------auto--------------------------------
    path('agregar-auto', views.agregar_auto, name='agregar_auto'),
    path('detalle-auto/<int:pk>', views.detalle_auto, name='detalle_auto'),
    path('listar-autos/',  views.listar_autos, name='listar_autos'),
    path('eliminar-auto/<int:pk>', views.eliminar_auto, name='eliminar_auto'),
    path('modificar-auto/<int:pk>', views.modificar_auto, name='modificar_auto'),
    # -----------------------servicios---------------------------------
    path('agregar-servicio/',  views.agregar_servicio, name='agregar_servicio'),
    path('detalle-servicio/<int:pk>/',  views.detalle_servicio, name='detalle_servicio'),
    path('listar-servicios/',  views.listar_servicios, name='listar_servicios'),
    path('modificar-servicio/<int:pk>/', views.modificar_servicio, name='modificar_servicio'),
    path('eliminar-servicio/<int:pk>/', views.eliminar_servicio, name='eliminar_servicio'),
    ]