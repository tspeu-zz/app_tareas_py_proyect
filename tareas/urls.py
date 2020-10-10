from django.urls import path, re_path
# 1 forma
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    # path('tareas/', views.tarea_list.as_view(), name='tarea_list'),
    path('', views.index, name='index'),
    # path('lista/<pk>/', views.lista_tareas, name='lista_tareas'),
    path('lista/', views.lista_tareas, name='lista_tareas'),
    path("add_tarea/", views.add_tarea, name="add_tarea"),
    path("update/<pk>/", views.update_task, name="update_tarea"),
    path("delete/<pk>/", views.delete_task, name="delete_tarea"),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('aviso/', views.aviso, name='aviso_legal'),
    path('contacto/', views.contacto, name='contacto'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
