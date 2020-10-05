# from datetimewidget.widgets import DateTimeWidget
# from bootstrap_datepicker.widgets import DatePicker
from datetime import datetime

from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
# from django.forms import extras


from django import forms
from django.forms import ModelForm, SelectDateWidget
from .models import Tareas

# date picket
class FechaInput(forms.DateInput):
    input_type = 'date'

#
class TaskForm(ModelForm):
    class Meta(object):
        model = Tareas
        # fields = "__all__"  # include all fields in form
        fields = ['nombre','descripcion', 'terminado', 'f_creado', 'f_entregado', 'f_final',
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
                    'class': 'form-control'
                }
            ),
            'terminado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'f_creado': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'text',
                    'class': 'form-control'
                },
                # options={
                #     'useCurrent': True,
                #     'collapse': False,
                # },
                # attrs={
                #     'append': 'fa fa-calendar',
                #     'icon_toggle': True,
                # }
            ),
            # 'f_entregado': FechaInput(),
            'f_entregado': DatePicker(
                options={
                    'minDate': '2009-01-20',
                    'maxDate': '2017-01-20',
                },
            ),
            'f_final': FechaInput(),
            # 'tipo_tarea':forms.

            #     'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),
            #     attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl',
            #     'format': 'yyyy-mm-dd', 'type': 'date'}),

        }
        # fields = ('nombre', 'terminado') # include particula
#  forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'onoffswitch','id': 'myonoffswitch'})
#  )
