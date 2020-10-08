from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import TaskForm, CreateUserForm, CreateForm
from .models import Tareas, Usuario
# register django default
from django.contrib.auth import authenticate, login, logout
# para retringir el usuario al acceso a las paginas
from django.contrib.auth.decorators import login_required

# retringir el accseso si el ususaio no está login se redirige a login
@login_required(login_url='login')
def lista_tareas(request):
    # _user = Usuario.objects.get(usuario_id=pk)
    # print('usuraio- > ', _user)
    form = TaskForm()
    # form = CreateForm()
    if request.method == 'POST':
        print('datos creados',  request.POST)
        form = TaskForm(request.POST)
        # form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')

    _tareas = Tareas.objects.all()
    print(_tareas)
    return render(request, "tareas.html",   {"task_form": form, "tareas": _tareas})


def index(request):
    # return HttpResponse("Hello World!!")
    # form = TaskForm()
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    #
    # _tareas = Tareas.objects.all()
    # print(_tareas)
    return render(request, "index.html")

#
@login_required(login_url='login')
def update_task(request, pk):
    task = Tareas.objects.get(id=pk)
    # form = TaskForm(instance=task)
    form = CreateForm(instance=task)
    print('form ' + form.__str__())
    print('task ' + task.__str__())
    print('id ' + pk)
    # user = task.cleaned_data.get('username')
    # user_id = task.cleaned_data.get('usuario_id')
    if request.method == "POST":
        # form = TaskForm(request.POST, instance=task)
        form = CreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("lista_tareas")

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


