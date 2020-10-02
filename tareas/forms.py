from django import forms
from django.forms import ModelForm
from .models import Tareas


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = "__all__"  # include all fields in form
        # fields = ('nombre', 'terminado') # include particula
