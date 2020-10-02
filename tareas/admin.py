from django.contrib import admin
from .models import TipoTarea, Asignatura, Usuario, Tareas
# Register your models here.
admin.site.register(TipoTarea)
admin.site.register(Asignatura)
admin.site.register(Usuario)
admin.site.register(Tareas)
