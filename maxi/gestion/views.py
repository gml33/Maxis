from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, autoForm, servicioForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import auto,empleado,servicio
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def home(request):
    return render(request, 'registro/index.html')

#register view

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context={'form':form}
    return render(request, 'registro/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                #bot.send_message(chat_id, text='Logueado')
                return redirect('dashboard')
    context = {'form':form}
    return render(request, 'registro/my-login.html', context=context)

@login_required(login_url='my-login')
def dashboard(request):
    autos_all = auto.objects.all().order_by('id')
    paginator = Paginator(autos_all, 10)
    page = request.GET.get('page')
    autos = paginator.get_page(page)
    context = {
        'autos':autos,
    }
    return render(request, 'gestion/dashboard.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('my-login')
#----------------------------autos-------------------------------

@login_required(login_url='my-login')
def agregar_auto(request):
    form = autoForm()
    if request.method == 'POST':
        form = autoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request, 'gestion/auto/agregar.html', context=context)

@login_required(login_url='my-login')
def eliminar_auto(request, pk):
    auto_seleccionado= auto.objects.get(id=pk)
    auto_seleccionado.delete()
    return redirect('dashboard')

@login_required(login_url='my-login')
def modificar_auto(request, pk):
    auto_seleccionado = auto.objects.get(id=pk)
    form = autoForm(instance=auto_seleccionado)
    if request.method == 'POST':
        form = autoForm(request.POST, instance=auto_seleccionado)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request, 'gestion/auto/modificar.html', context=context)

@login_required(login_url='my-login')
def detalle_auto(request, pk):
    auto_seleccionado = auto.objects.get(id=pk)    
    context = {
        'auto':auto_seleccionado
    }
    return render(request, 'gestion/auto/detalle.html', context=context)

@login_required(login_url='my-login')
def listar_autos(request):
    autos_all = auto.objects.all().order_by('id')
    paginator = Paginator(autos_all, 10)
    page = request.GET.get('page')
    autos = paginator.get_page(page)
    context = {
        'autos':autos,
    }
    return render(request, 'gestion/auto/listar.html', context=context)


#----------------------------servicios-------------------------------

@login_required(login_url='my-login')
def agregar_servicio(request):
    form = servicioForm()
    if request.method == 'POST':
        form = servicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_servicios')
    context = {
        'form':form
    }
    return render(request, 'gestion/servicio/agregar.html', context=context)

@login_required(login_url='my-login')
def eliminar_servicio(request, pk):
    servicio_seleccionado= servicio.objects.get(id=pk)
    servicio_seleccionado.delete()
    return redirect('dashboard')

@login_required(login_url='my-login')
def modificar_servicio(request, pk):
    servicio_seleccionado = servicio.objects.get(id=pk)
    form = servicioForm(instance=servicio_seleccionado)
    if request.method == 'POST':
        form = servicioForm(request.POST, instance=servicio_seleccionado)
        if form.is_valid():
            form.save()
            return redirect('listar_servicios')
    context = {
        'form':form
    }
    return render(request, 'gestion/servicio/modificar.html', context=context)

@login_required(login_url='my-login')
def detalle_servicio(request, pk):
    servicio_seleccionado = servicio.objects.get(id=pk)
    context = {
        'servicio':servicio_seleccionado
    }
    return render(request, 'gestion/servicio/detalle.html', context=context)

@login_required(login_url='my-login')
def listar_servicios(request):
    servicios_all = servicio.objects.all().order_by('-fecha')
    paginator = Paginator(servicios_all, 10)
    page = request.GET.get('page')
    servicios = paginator.get_page(page)
    context = {
        'servicios':servicios,
    }
    return render(request, 'gestion/servicio/listar.html', context=context)

@login_required(login_url='my-login')
def service(request):
    vehiculo = request.POST.get['patente']  
    servicio_vehiculo = servicio.objects.filter(vehiculo=vehiculo).order_by('-fecha')
    paginator = Paginator(servicio_vehiculo, 10)
    page = request.GET.get('page')
    servicios = paginator.get_page(page)
    context = {
        'servicios':servicios,
    }
    return render(request, 'gestion/servicio/listar.html', context=context)