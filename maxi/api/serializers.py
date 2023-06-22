from rest_framework import serializers
from .models import auto, empleado, servicio

class servicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=servicio
        fields = '__all__'

class empleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=empleado
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = auto
        fields = '__all__'