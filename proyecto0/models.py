from django.db import models

class Evento(models.Model):

    CATEGORIAS = (
        ('Conferencia', 'Conferencia'),
        ('Seminario', 'Seminario'),
        ('Congreso', 'Congreso'),
        ('Curso', 'Curso'),
    )

    MODALIDAD = (
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
    )


    id = models.AutoField(auto_created=True, primary_key=True)
    nombre_evento = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=100, choices=MODALIDAD)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS)
    lugar = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    username = models.CharField(max_length=100)


    def trae_direccion_evento(self):
    	return self.direccion

