from django.forms import ModelForm
from piso.models import Piso, Gastosmensuales, Tareas, Listacompra, Notas
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
#exclude =["user", "bottle"]

class forma(ModelForm):
	class Meta:
		model = Piso
		fields = {'Direccion','Precio','nombre'}


class SingUpForm(ModelForm):
        password = forms.CharField(widget=forms.PasswordInput(render_value = False), required = True) 
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name']	
		widgets = {
			'password': forms.PasswordInput(),		
		}

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())


class formArt(ModelForm):
	class Meta:
		model = Gastosmensuales
		fields = {'Mes', 'PrecioPiso','PrecioGas','PrecioLuz','PrecioInternet', 'PrecioTotal'}
		widgets = {'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),}


class formNot(ModelForm):
	class Meta:
		model = Notas
		fields = {'Texto', 'fecha'}
		widgets = {'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),}


class formTar(ModelForm):
	class Meta:
		model = Tareas
		fields = {'Limpieza', 'Basura', 'Extra', 'Semana', 'MesTarea'}
		widgets = {'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),}

class formLcpra(ModelForm):
	class Meta:
		model = Listacompra
		fields = {'DineroPersona', 'Productos', 'fechalista'}
		widgets = {'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),}

