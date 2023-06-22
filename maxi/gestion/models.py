from django.db import models

class auto(models.Model):
    patente=models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.patente}"

class empleado(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class servicio(models.Model):
    vehiculo = models.ForeignKey(auto, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=False)
    detalle = models.TextField()
    empleado = models.ForeignKey(empleado, on_delete=models.CASCADE, blank=False)
    kilometraje = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.vehiculo} - {self.fecha}"

