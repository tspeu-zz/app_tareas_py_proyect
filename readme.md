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
  
git remote add origin git@github.com:tspeu/test_py_proyect.git
git push -u origin main   