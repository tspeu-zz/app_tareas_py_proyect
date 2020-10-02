from django.urls import path, re_path
# 1 forma
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    # path('tareas/', views.tarea_list.as_view(), name='tarea_list'),
    path('tareas/', views.tarea_list, name='tarea_list'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
