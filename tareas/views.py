from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskForm, CreateUserForm, CreateForm
from .models import Tareas, Usuario
from django.contrib.auth import authenticate, login, logout
# para retringir el acceso a las paginas
from django.contrib.auth.decorators import login_required
from datetime import date

"""
retringir el acceso si el usuario no está login. se redirige a login page
"""
@login_required(login_url='login')
def lista_tareas(request):
    """
        muestra la lista de las tareas del usuario
    """
    form = TaskForm()
    usuario = request.user
    _tareas = Tareas.objects.filter(usuario_id=usuario.usuario_id)
    return render(request, "tareas.html",  {"task_form": form, "tareas": _tareas})


@login_required(login_url='login')
def index(request):
    """
    landing page
    """
    usuario = request.user
    context = {'usuario': usuario}
    return render(request, "index.html", context)


def add_tarea(request):
    """
    añadir una nueva tarea asignada al usuario
    """
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    form = CreateForm()
    _user = Usuario.usuario_id
    context = {'form': form, 'day_today': d1}

    if request.method == "POST":
        __datos = request.POST
        form = CreateForm(__datos)
        form.usuario = request.user
        # print(' form.errors--> ', form.errors)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.usuario = request.user
            thought.save()
            return redirect("lista_tareas")

    return render(request, "add_tarea.html", context)


#
@login_required(login_url='login')
def update_task(request, pk):
    """
    actualizar una tarea
    :param request:
    :param pk: int. el id de la tarea.  el pasa en la url
    :return:
    """
    task = Tareas.objects.get(id=pk)
    form = CreateForm(instance=task)

    if request.method == "POST":
        form = CreateForm(request.POST, instance=task)

        if form.is_valid():

            form.save()
            return redirect("lista_tareas")
        # else:
            # print(' form.errors--> ', form.errors)

    return render(request, "update.html", {"task_edit_form": form})

#
@login_required(login_url='login')
def delete_task(request, pk):
    """
    eliminar una tarea
    :param request:
    :param pk: el id de la tarea. se pasa por la url
    :return:
    """
    tarea = Tareas.objects.get(id=pk)
    if request.method == "POST":
        tarea.delete()
        return redirect("lista_tareas")

    context = {'item': tarea}
    return render(request, "delete.html", context)


def register_page(request):
    """
    registrar un nuevo usuario.
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'La cuenta se ha creado con éxito! Bienvenido ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    """
    login de usuario, usando username y contraseña
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            usern = request.POST.get('username')
            passw = request.POST.get('password')

            user = authenticate(request, username=usern, password=passw)
            # validar
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'usuario o constraseña incorrecta')

        context = {}
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def aviso(request):
    """
    página de aviso legal. por construir
    :param request:
    :return:
    """
    return render(request, "aviso_legal.html")


@login_required(login_url='login')
def contacto(request):
    """
    página de contacto. por construir
    :param request:
    :return:
    """
    return render(request, "contacto.html")
