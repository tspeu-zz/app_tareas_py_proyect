from rest_framework import serializers

from tareas.models import Tareas, Asignatura, TipoTarea, Usuario

class TareaSerialize(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = ('nombre', 'descripcion', 'terminado', 'f_creado', 'f_entregado', 'f_final', 'tipo_tarea', 'asignatura', 'usuario')


class AsignaturaSerialize(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('nombre', 'active')


class TipoTareaSerialize(serializers.ModelSerializer):
    class Meta:
        model = TipoTarea
        fields = ('nombre', 'active')


class UsuarioSerialize(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'email', 'active')


