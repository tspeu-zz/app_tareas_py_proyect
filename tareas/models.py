from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

# Create your models here.
#
class TipoTarea(models.Model):
    nombre = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f' {self.nombre}'


#
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.nombre}, {self.email} {self.active}'


#
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f' {self.nombre}'

# naming: you should name your model in single form, not plural (Article instead of Articles)
# default=timezone.now
class Tareas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    terminado = models.BooleanField(default=False)
    # f_creado = models.DateTimeField(auto_now_add=True, auto_now=False)
    f_creado = models.DateField(auto_now_add=False, auto_now=False)
    # f_entregado = models.DateTimeField(auto_now_add=False, auto_now=True)
    f_entregado = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    # f_final = models.DateTimeField(auto_now_add=False, auto_now=True)
    f_final = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    tipo_tarea = models.ManyToManyField(TipoTarea, help_text="escoger un tipo de tarea")
    asignatura = models.ManyToManyField(Asignatura, help_text="escoger una asignatura")
    usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, null=False)
#

#
    def __str__(self):
        return f' {self.nombre},{self.descripcion}, {self.terminado},{self.f_creado}, {self.f_entregado}, {self.f_final} '

#
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de una tarea.
        """
        return reverse('tarea-detail', args=[str(self.id)])
#