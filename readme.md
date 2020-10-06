#crear entorno virtual eparado del proyecto
http://blog.enriqueoriol.com/2015/01/django-1.7-intro-django-rest-framework.html
https://www.codesnail.com/todo-app-in-django-part-1-django-installation-and-setup/

pip install django

pip install djangorestframework

django-admin.py startproject encuesta_projecto .

django-admin.py startproject practica_agenda .
 
 ** app encuesta
 manage.py startapp encuestas
 manage.py startapp api
 
 
INSTALLED_APPS = [
    'rest_framework'
    'api'
 
django.conf.urls.defaults

# estructura de db
manage.py makemigrations
# se pasa los datos a la db
manage.py migrate

manage.py runserver

manage.py createsuperuser
root - 1234

{
"title": "The first survey",
"question": "Are you happy right now?",
"owner": "Marcus",
"active": true
}

{
"title": "otra encuesta",
"question": "esto es nuevo?",
"owner": "pepe",
"active": true
}

* practica
*  manage.py startapp agenda
add agenda to settings 

{
"nombre": "pepe",
"telefono": "34 45555551",
"active": true
}
#
yo he leído que es para darle un nombre a la ruta
y se podría acceder a travez de la app. es decir encuesta.lista_encuesta
https://stackoverflow.com/questions/46729889/what-does-name-mean-in-django-url

<a href="{% url 'encuesta.lista_encuesta' %}">Go to main</a>

sería una ruta interna, parece


manage.py makemigrations
manage.py migrate
jm
1234


#
una curiosidad , si se añade
urlpatterns = format_suffix_patterns(urlpatterns)

se puede muestra en formato json
http://127.0.0.1:8000/api/encuestas.json
o así 
http://127.0.0.1:8000/api/encuestas/?format=json

#
 *args, por referencia
 **kwargs para usar clave valor
 
 
 usando mixings
 ListCreateAPIView para listar y crear  get post
 RetrieveUpdateDestroyAPIView para put/ delete
 
 queryset debe llamase así
 
 crear un usuario para la API con permisos especiales
 
 https://www.django-rest-framework.org/api-guide/generic-views/
 
 from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)


  manage.py createsuperuser
  
  crear pagina inicio
  ir a url.py del proyecto
  



https://pypi.org/project/django-tempus-dominus/
pip install django-tempus-dominus
Then add tempus_dominus to INSTALLED_APPS in your Django settings.


git remote add origin git@github.com:tspeu/test_py_proyect.git
git push -u origin main   


pepe
9SqLuZZ7XZy6DL8

# register djnago create user
test 
9SqLuZZ7XZy6DL8
