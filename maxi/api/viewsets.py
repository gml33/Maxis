from rest_framework import viewsets
from .models import auto, empleado, servicio
from .serializers import AutoSerializer, empleadoSerializer, servicioSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = auto.objects.all()
    serializer_class = AutoSerializer

class empleadoViewSet(viewsets.ModelViewSet):
    queryset = empleado.objects.all()
    serializer_class = empleadoSerializer

class servicioViewSet(viewsets.ModelViewSet):
    queryset = servicio.objects.all()
    serializer_class = servicioSerializer