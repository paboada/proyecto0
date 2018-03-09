from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .models import Evento
from django.http import HttpResponse
from django.contrib.auth.models import User
from .import forms #importo las formas creadas en forms.py
from django.contrib.auth.decorators import login_required 
import re
from django.contrib import messages


# Create your views here.
#registrar usuarios
def form_registrar_usuario(request):
	if request.method == 'POST':
		formulario_registro = UserCreationForm(request.POST)
		if formulario_registro.is_valid():
			print(request.POST.get('username'))
			patron_correo = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
			cumple_patron = patron_correo.match(request.POST.get('username'))
			print(cumple_patron)
			if cumple_patron:
				#guarda el usuario en la base de datos
				user = formulario_registro.save()
				login(request,user)
				messages.success(request, 'Gracias por registrarte!!!!!')
				return redirect('agenda_eventos:login') #Lo envio a la pantalla de ingreso de usuarios ya registrados
			else:
				messages.info(request, 'El registro debe realizarse con un correo electronico valido')
	else:
		formulario_registro = UserCreationForm()
	return render(request,'nuevousuario.html',{'formulario_registro':formulario_registro})

#login
def formulario_ingresar_usuario(request):
	if request.method == 'POST':
		formulario_ingreso = AuthenticationForm(data=request.POST)
		if formulario_ingreso.is_valid(): #si el usuario y password son correctos
			#login
			user = formulario_ingreso.get_user()
			login(request,user) #usado para quedar loqueado en la aplicacion de admin
			#eventos = Evento.objects.filter(username = user).order_by('fecha_inicio') #envio solo eventos del usuario login
			#return render(request, 'lista_eventos.html', {'eventos':eventos, 'usuario': user})
			return redirect('agenda_eventos:lista_eventos') #hacia urls.py para name = lista_eventos
	else:
		formulario_ingreso = AuthenticationForm()
	return render(request,'login.html',{'formulario_ingreso':formulario_ingreso})

#logout
def logout_view(request):
	logout(request)
	return redirect('agenda_eventos:lista_eventos') #hacia urls.py para name = lista_eventos

#Crear evento
@login_required(login_url="login/")
def formulario_crear_evento(request):
	if request.method == 'POST':
		formulario_crear = forms.CrearEvento(data=request.POST)
		print(request.POST.get('fecha_inicio'))
		if formulario_crear.is_valid():
			form = formulario_crear.save(commit=False) #crea el elemnto, lo captura sin dar commit para modificar campos
			form.username = request.user #como no hice commit, tomo lo guardado y le asigno el usuario logueado
			form.save() #guardo en db
			return redirect('agenda_eventos:lista_eventos' ) #despues de guardarlo, envio al usuario a la lista de eventos
	else:
		form_crear_evento = forms.CrearEvento()
	return render(request, 'crearevento.html', {'form_crear_evento':form_crear_evento})




#Si el usuario hace login correctamente, se dirige a este metodo y lista los eventos registrados para el usuario logueado
#Ordena los eventos por la fecha de inicio del mismo
@login_required(login_url="login/")
def traer_lista_eventos(request):
	current_user = request.user
	eventos = Evento.objects.filter(username = current_user).order_by('fecha_inicio')
	return render(request, 'lista_eventos.html', {'eventos':eventos})

@login_required(login_url="login/")
def traer_detalle_evento(request, id_evento):
	id_elegido = id_evento
	evento = Evento.objects.filter(id = id_elegido)
	return render(request, 'detalle_evento.html', {'evento':evento})

def borrar_evento(request, id_evento):
	id_elegido = id_evento
	evento = Evento.objects.filter(id = id_elegido)
	evento.delete()
	current_user = request.user
	eventos = Evento.objects.filter(username = current_user).order_by('fecha_inicio')
	return render(request, 'lista_eventos.html', {'eventos':eventos})

def formulario_editar_evento(request, id_evento):
	if request.method == 'POST':
		formulario_edicion = forms.EditarEvento(data=request.POST)
		if formulario_edicion.is_valid():
			form = formulario_edicion.save(commit=False)
			form.id = id_evento
			form.save()
			return redirect('agenda_eventos:lista_eventos' ) #despues de guardarlo, envio al usuario a la lista de eventos
	else:
		current_user = request.user
		eventos = Evento.objects.filter(id = id_evento)
		formulario_edicion = forms.EditarEvento()
	return render(request, 'editar_evento.html', {'formulario_edicion':formulario_edicion , 'eventos':eventos })