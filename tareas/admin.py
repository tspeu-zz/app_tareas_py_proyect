from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TipoTarea, Asignatura, Usuario, Tareas
# Register your models here.
admin.site.register(TipoTarea)
admin.site.register(Asignatura)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Tareas)
