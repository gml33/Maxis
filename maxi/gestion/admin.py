from django.contrib import admin
from .models import auto, empleado, servicio

# Register your models here.

class autoadmin(admin.ModelAdmin):
    list_display = ["patente"]
    search_fields = ["patente"]
    list_filter = ["patente"]
    list_per_page = 50

class empleadoadmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido"]
    search_fields = ["nombre", "apellido"]
    list_filter = ["nombre", "apellido"]
    list_per_page = 50

class servicioadmin(admin.ModelAdmin):
    list_display = ["vehiculo", "fecha", "empleado"]
    search_fields = ["vehiculo", "fecha", "empleado"]
    list_filter = ["vehiculo", "fecha", "empleado"]
    list_per_page = 50

admin.site.register(auto, autoadmin)
admin.site.register(empleado, empleadoadmin)
admin.site.register(servicio, servicioadmin)