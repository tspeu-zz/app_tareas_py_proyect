from django.urls import path, re_path
# 1 forma
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    # path('tareas/', views.tarea_list.as_view(), name='tarea_list'),
    path('', views.lista_tareas, name='lista_tareas'),
    path("update/<pk>/", views.update_task, name="update_task"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
