from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render
from forms import forma, formArt, formNot, formTar, formLcpra
# Create your views here.

def inicial(request):
	if not request.user.is_anonymous():
		n=True
	return render_to_response("piso/indice.html",locals(),context_instance=RequestContext(request))




def login(request):
	from piso.models import Piso

	if not request.user.is_anonymous():
		return HttpResponseRedirect('')
	if request.method=='POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			clave = request.POST['password']
			user = authenticate(username=username, password=clave)
			if user is not None:
				if user.is_active:
					auth_login(request, user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/')
			else:
					return HttpResponseRedirect('/')

	else:
		form= AuthenticationForm()
	return render_to_response('piso/login.html', locals(), context_instance=RequestContext(request))



def nuevoUser(request):
	from piso.models import Piso


	if request.method == 'POST':


		form = UserCreationForm(request.POST)
 		if form.is_valid():
			username = request.POST['username']
			
			npiso=Piso(user=username,Direccion="indefinido",Precio=500, nombre="indefinido")
			npiso.save()
 			form.save()
 			return HttpResponseRedirect('/login/')
 	else:
 		form=UserCreationForm()
 	return render_to_response('piso/usuario.html', locals(), context_instance=RequestContext(request))




def cerrar(request):
	logout(request)
	return render_to_response('piso/indice.html', context_instance=RequestContext(request))






def crear(request):
	from piso.models import Piso
	usuarios = request.user

	if not request.user.is_anonymous():
		n=True
		usuari = str(usuarios)
		ad=Piso.objects.get(user=usuari)
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/piso/login')
	if request.method=='POST':

		form = forma(request.POST, request.FILES)

		if form.is_valid():
			
			dire = request.POST['Direccion']
			pre=request.POST['Precio']
			nom=request.POST['nombre']
			ec=Piso.objects.get(user=usuarios)
   			ec.Direccion=dire 
			ec.Precio=pre
			ec.nombre=nom
    			ec.save()
			
		return HttpResponseRedirect('/')
	else:
		form = forma()

	return render_to_response('piso/crear.html', locals(), context_instance=RequestContext(request))
# Create your views here.











def mostrar(request):
	from piso.models import Piso

	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Piso.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/piso/login')
	nombre=Piso.objects.get(user=usuarios)

	return render_to_response('piso/mostrar.html', locals(), context_instance=RequestContext(request))




def creargastosmensuales(request):
	from piso.models import Piso, Gastosmensuales
	gastosmen=Gastosmensuales.objects.all()
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Piso.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/piso/login')
	if request.method=='POST':
		
		form = formArt(request.POST, request.FILES)

		if form.is_valid():
			
			me= request.POST['Mes']
			prepi = request.POST['PrecioPiso']
			pregas= request.POST['PrecioGas']
			prelu= request.POST['PrecioLuz']
			prein= request.POST['PrecioInternet']
			preto= request.POST['PrecioTotal']
			gasto=Gastosmensuales()
			gasto.Mes=me
			gasto.PrecioPiso=prepi
			gasto.PrecioGas=pregas
			gasto.PrecioLuz=prelu
			gasto.PrecioInternet=prein
			gasto.PrecioTotal=preto
			gasto.Pisos=ad
			gasto.save()
			return HttpResponseRedirect('/')
		
	else:
		form = formArt()
	nombre=Piso.objects.get(user=usuarios)
	dinero=Gastosmensuales.objects.filter(Pisos=nombre)
	return render_to_response('piso/mostrargastosmensuales.html', locals(), context_instance=RequestContext(request))






def notas(request):
	from piso.models import Piso, Notas
	notitas=Notas.objects.all()
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Piso.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/piso/login')
	if request.method=='POST':
		
		form = formNot(request.POST, request.FILES)

		if form.is_valid():
			
			txt = request.POST['Texto']
			fch = request.POST['fecha']
			tex=Notas()
			tex.Texto=txt
			tex.fecha=fch
			tex.Pisos=ad
			tex.save()
			return HttpResponseRedirect('/')
		
	else:
		form = formNot()
	nombre=Piso.objects.get(user=usuarios)
	notis=Notas.objects.filter(Pisos=nombre)
	return render_to_response('piso/notas.html', locals(), context_instance=RequestContext(request))




def limpiezahogar(request):
	from piso.models import Piso, Tareas
	tareitas=Tareas.objects.all()
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Piso.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/piso/login')
	if request.method=='POST':
		
		form = formTar(request.POST, request.FILES)

		if form.is_valid():
			
			lmpi = request.POST['Limpieza']
			basu = request.POST['Basura']
			ext = request.POST['Extra']
			smn = request.POST['Semana']
			mtr = request.POST['MesTarea']
			limp=Tareas()
			limp.Limpieza=lmpi
			limp.Basura=basu
			limp.Extra=ext
			limp.Semana=smn
			limp.MesTarea=mtr
			limp.Pisos=ad
			limp.save()
			return HttpResponseRedirect('/')
	else:
		form = formTar()
	nombre=Piso.objects.get(user=usuarios)
	tar=Tareas.objects.filter(Pisos=nombre)
	return render_to_response('piso/limpieza.html', locals(), context_instance=RequestContext(request))



def liscomp(request):
	from piso.models import Piso, Listacompra
	Lstcmpr=Listacompra.objects.all()
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Piso.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/piso/login')
	if request.method=='POST':
		
		form = formLcpra(request.POST, request.FILES)

		if form.is_valid():
			
			dper = request.POST['DineroPersona']
			produ = request.POST['Productos']
			feclst = request.POST['fechalista']
			liscm=Listacompra()
			liscm.DineroPersona=dper
			liscm.Productos=produ
			liscm.fechalista=feclst
			liscm.Pisos=ad
			liscm.save()
			return HttpResponseRedirect('/')
	else:
		form = formLcpra()
	nombre=Piso.objects.get(user=usuarios)
	ltcm=Listacompra.objects.filter(Pisos=nombre)
	return render_to_response('piso/listacompra.html', locals(), context_instance=RequestContext(request))


