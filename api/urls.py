from django.urls import path, re_path
# 1 forma
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    # path('tareas/', views.tarea_list.as_view(), name='tarea_list'),
    path('tareas/', views.TareaList.as_view(), name='tarea_list'),
    path('tareas/<pk>', views.TareaDetalle.as_view(), name='tarea_detalle'),
    path('tipo_tareas/', views.TipoTareaLista.as_view(), name='tipo_tarea_list'),
    path('tipo_tareas/<pk>', views.TipoTareaDetalle.as_view(), name='tipo_tarea_detalle'),
    path('asignatura/', views.AsignaturaLista.as_view(), name='asignatura_list'),
    path('asignatura/<pk>', views.AsignaturaDetalle.as_view(), name='asignatura_detalle'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
