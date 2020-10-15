#App Tarea Pendientes
App para registras y controlar las tereas pendientes



pip install django

pip install djangorestframework

django-admin.py startproject nombre_projecto .

manage.py makemigrations
manage.py migrate

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)

manage.py createsuperuser
manage.py runserver
  
git remote add origin git@github.com:https://github.com/tspeu/app_tareas_py_proyect
git push -u origin main   

git remote set-url origin git@github.com:User/project-new.git
git remote set-url origin git@github.com:tspeu/app_tareas_py_proyect