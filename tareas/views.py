from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import TaskForm, CreateUserForm, CreateForm
from .models import Tareas, Usuario
# register django default
from django.contrib.auth import authenticate, login, logout
# para retringir el usuario al acceso a las paginas
from django.contrib.auth.decorators import login_required
from datetime import date

# retringir el accseso si el ususaio no está login se redirige a login
@login_required(login_url='login')
def lista_tareas(request):

    form = TaskForm()
    # _tareas = Tareas.objects.all()
    usuario = request.user
    print('usuario --->', usuario.usuario_id)
    _tareas = Tareas.objects.filter(usuario_id=usuario.usuario_id)
    print(_tareas)
    return render(request, "tareas.html",   {"task_form": form, "tareas": _tareas})


@login_required(login_url='login')
def index(request):
    usuario = request.user
    context = {'usuario': usuario}
    return render(request, "index.html", context)


#
"""
"""


def add_tarea(request):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    print("d1 =", d1)
    form = CreateForm()
    _user = Usuario.usuario_id
    print("_user =", _user)
    # form.fields['f_creado'].initial = d1
    # form.fields['f_entregado'].initial = d1
    context = {'form': form, 'day_today': d1}

    if request.method == "POST":
        __datos = request.POST
        print('datos --> ', __datos)
        # text = request.POST['text']
        form = CreateForm(__datos)
        form.usuario = request.user
        print('form dataaaaa--> ', form.data)
        print(' form.errors--> ', form.errors)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.usuario = request.user
            print('thought.usuario --> ', thought.usuario)
            thought.save()
            # form.save()
            print('form validoo --> ', form.data)
            return redirect("lista_tareas")
        # else:
        #     print('NOOOOO form validoooo --> ',)

    return render(request, "add_tarea.html", context)


#
@login_required(login_url='login')
def update_task(request, pk):
    task = Tareas.objects.get(id=pk)
    form = CreateForm(instance=task)
    print('task ', task.__str__())
    print('id ' + pk)
    if request.method == "POST":
        print('form -->', request.POST)
        form = CreateForm(request.POST, instance=task)
        # form.save()
        # return redirect( "lista_tareas")
        if form.is_valid():
            # thought = form.save(commit=False)
            # thought.usuario = request.user
            # print('thought.usuario --> ', thought.usuario )
            # thought.save()
            form.save()
            return redirect("lista_tareas")
        else:
            print("no valido update", )
            print(' form.errors--> ', form.errors)
        #     print('form -->', request.POST)

    return render(request, "update.html", {"task_edit_form": form})

#
@login_required(login_url='login')
def delete_task(request, pk):
    tarea = Tareas.objects.get(id=pk)
    if request.method == "POST":
        tarea.delete()
        return redirect("lista_tareas")

    context = {'item': tarea}
    return render(request, "delete.html", context)


def register_page(request):
    """
    registrar un usuerio
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

    # login user
def login_page(request):
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

#
def logout_user(request):
    logout(request)
    return redirect('login')


#
@login_required(login_url='login')
def aviso(request):
    return render(request, "aviso_legal.html")

@login_required(login_url='login')
def contacto(request):
    return render(request, "contacto.html")
