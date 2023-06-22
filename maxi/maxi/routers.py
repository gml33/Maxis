from rest_framework import routers
from gestion.viewsets import AutoViewSet, empleadoViewSet, servicioViewSet

router = routers.DefaultRouter()

router.register(r'Auto', AutoViewSet)
router.register(r'empleado', empleadoViewSet)
router.register(r'servicio', servicioViewSet)