from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import *

#register/create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email','password1', 'password2']

#login user
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())



class autoForm(forms.ModelForm):  
    
    class Meta:
        model=auto
        fields = '__all__'

class servicioForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  
    
    class Meta:
        model=servicio
        fields = '__all__'


class empleadoForm(forms.ModelForm):
    apellido = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))  
    
    class Meta:
        model=empleado
        fields = '__all__'