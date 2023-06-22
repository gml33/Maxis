from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for auto
from .serializers import AutoSerializer, empleadoSerializer, servicioSerializer
# auto model
from .models import auto, empleado, servicio



@csrf_exempt
def autos(request):
    if(request.method == 'GET'):
        # get all the autos
        autos = auto.objects.all()
        # serialize the auto data
        serializer = AutoSerializer(autos, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = AutoSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def detalle_auto(request, pk):
    try:
        # obtain the auto with the passed id.
        auto = auto.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = AutoSerializer(auto, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the auto
        auto.delete() 
        # return a no content response.
        return HttpResponse(status=204)



@csrf_exempt
def empleados(request):
    if(request.method == 'GET'):
        empleados = empleado.objects.all()
        serializer = empleadoSerializer(empleados, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = empleadoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def servicios(request):
    if(request.method == 'GET'):
        servicios = servicio.objects.all()
        serializer = servicioSerializer(servicios, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = servicioSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def detalle_servicio(request, pk):
    try:
        # obtain the auto with the passed id.
        servicio = servicio.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = servicioSerializer(servicio, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the auto
        servicio.delete() 
        # return a no content response.
        return HttpResponse(status=204)