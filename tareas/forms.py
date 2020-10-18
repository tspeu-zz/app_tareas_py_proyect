# from datetimewidget.widgets import DateTimeWidget
# from bootstrap_datepicker.widgets import DatePicker
# from datetime import datetime

# from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
# from django.forms import extras


from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Tareas, Usuario
# from django.contrib.auth.models import User

# date picket
class FechaInput(forms.DateInput):
    """
        clase para personalizar el elemeto de seleccion de fecha
    """
    input_type = 'date'

#
class TaskForm(ModelForm):
    """
    formulario de prueba
    """
    class Meta(object):
        model = Tareas
        # fields = "__all__"  # include all fields in form
        fields = ['nombre', 'descripcion', 'terminado', 'f_creado', 'f_entregado', 'f_final',
                  'tipo_tarea', 'asignatura', 'usuario']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    # 'style': 'border-color: blue;',
                    'placeholder': 'escribir el nombre de la tarea'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols': "4",
                    'rows': "4"
                }
            ),
            'terminado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'f_creado': FechaInput(),
            'f_entregado': FechaInput(),
            'f_final': FechaInput(),
            'tipo_tarea': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'asignatura': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'usuario': forms.TextInput(
                attrs={
                    'style': 'border-color: blue;',
                })
        }


class CreateUserForm(UserCreationForm):
    """
    formualrio para el registro de una usuario
    """
    # username = forms.EmailField(label="nombre de usuario")
    # username = forms.EmailField(label="nombre de usuario")
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        # fields = '__all__'


class CreateForm(ModelForm):
    """
        formulario para la creacion de tareas y para la actualizacion de una tarea
    """
    class Meta:
        model = Tareas
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols': "2",
                    'rows': "2"
                }
            ),
            'f_creado': FechaInput(),
            'f_entregado': FechaInput(),
            'f_final': FechaInput(),
            'tipo_tarea': forms.SelectMultiple(
                attrs={'class': 'form-control'}
            ),
            'asignatura': forms.SelectMultiple(
                attrs={'class': 'form-control'}
            ),
        }
