# from datetimewidget.widgets import DateTimeWidget
# from bootstrap_datepicker.widgets import DatePicker
from datetime import datetime

# from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
# from django.forms import extras


from django import forms
from django.forms import ModelForm, SelectDateWidget
from django.contrib.auth.forms import UserCreationForm, UserModel
from .models import Tareas, Usuario
# from django.contrib.auth.models import User

# date picket
class FechaInput(forms.DateInput):
    input_type = 'date'

#
class TaskForm(ModelForm):
    class Meta(object):
        model = Tareas
        # fields = "__all__"  # include all fields in form
        fields = ['nombre', 'descripcion', 'terminado', 'f_creado', 'f_entregado', 'f_final',
                  'tipo_tarea', 'asignatura', 'usuario']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color: blue;',
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
        #     'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),
        #     attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl',
        #     'format': 'yyyy-mm-dd', 'type': 'date'}),
        # fields = ('nombre', 'terminado') # include particula
#  forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'onoffswitch','id': 'myonoffswitch'})
#  )
class CreateUserForm(UserCreationForm):

    # username = forms.EmailField(label="nombre de usuario")
    # username = forms.EmailField(label="nombre de usuario")
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        # fields = '__all__'


class CreateForm(ModelForm):

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
