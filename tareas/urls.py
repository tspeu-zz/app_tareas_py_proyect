from django.urls import path, re_path
# 1 forma
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    # path('tareas/', views.tarea_list.as_view(), name='tarea_list'),
    path('', views.lista_tareas, name='lista_tareas'),
    path("update/<pk>/", views.update_task, name="update_task"),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
