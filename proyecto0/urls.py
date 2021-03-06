from django.contrib import admin
from django.conf.urls import url
from proyecto0 import views

app_name = 'agenda_eventos'

urlpatterns = [
    url(r'login/',views.formulario_ingresar_usuario, name = 'login'),
    url(r'logout/',views.logout_view, name = 'logout'),
	url(r'registrousuario/',views.form_registrar_usuario),
	url(r'listaeventos/',views.traer_lista_eventos, name = 'lista_eventos'),
	url(r'creareventos/',views.formulario_crear_evento, name = 'crear_eventos'),
	url(r'^(?P<id_evento>[\w-]+)/$',views.traer_detalle_evento, name = 'detalle_evento'),
    url(r'^borrar/(?P<id_evento>\d+)/$',views.borrar_evento, name = 'borrar'),
    url(r'^editar/(?P<id_evento>\d+)/$',views.formulario_editar_evento, name = 'editar'),


]
