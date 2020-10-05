from django import forms
from django.forms import ModelForm
from .models import Tareas


class TaskForm(forms.ModelForm):
    class Meta(object):
        model = Tareas
        fields = "__all__"  # include all fields in form
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
                        'class': 'custom-control-input'

                    }
                )
        }
        # fields = ('nombre', 'terminado') # include particula
#  forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'onoffswitch','id': 'myonoffswitch'})
#  )