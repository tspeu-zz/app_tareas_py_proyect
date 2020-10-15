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

pip install gunicorn
pip install django-heroku
heroku create
#
https://polar-tor-42801.herokuapp.com/ | https://git.heroku.com/polar-tor-42801.git
#
heroku git:remote -a nombre_app_heroku
cambiar dev to production
gunicorn todo_app_proyect.wsgi.py --solo LINUX
crear Procfile
## probar 
heroku local  ... run in local
 pip freeze > requirements.txt
 runtime.txt -> para indicar la verion de python
## para indows..error ..waitress-serve --listen=*:8000 todo_app_proyect.wsgi:application
add settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

whitenoise.middleware.WhiteNoiseMiddleware