from django import forms
from .models import models
from proyecto0 import models
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms import ModelForm, Textarea, TextInput, DateTimeField, PasswordInput, DateTimeInput, Form


class CrearEvento(forms.ModelForm):
	class Meta:
		model = models.Evento
		fields = ['nombre_evento','modalidad','categoria','lugar','direccion','fecha_inicio','fecha_fin']
		widgets = {
		'fecha_fin' : forms.DateTimeInput(attrs={'placeholder': '2006-10-25 14:30:59' , 'id': 'fecha_fin' , 'onchange': 'return validacion(this.value)' }),
		'fecha_inicio' : forms.DateTimeInput(attrs={'placeholder': '2006-10-25 14:30:59' , 'id': 'fecha_inicio' , 'onchange': 'return validacion(this.value)' }),
		}

class EditarEvento(forms.ModelForm):
	class Meta:
		model = models.Evento
		fields = ['nombre_evento','modalidad','categoria','lugar','direccion','fecha_inicio','fecha_fin', 'username']
		widgets = {
		'fecha_inicio' : forms.DateTimeInput(attrs={'placeholder': '2006-10-25 14:30:59' , 'id': 'fecha_inicio' , 'onchange': 'return validacion(this.value)' }),
		'fecha_fin' : forms.DateTimeInput(attrs={'placeholder': '2006-10-25 14:30:59' , 'id': 'fecha_fin' , 'onchange': 'return validacion(this.value)' }),
		}