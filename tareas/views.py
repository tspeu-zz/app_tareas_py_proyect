from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import TaskForm, CreateUserForm
from .models import Tareas
# register django default
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def lista_tareas(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')

    _tareas = Tareas.objects.all()
    print(_tareas)
    return render(request, "index.html",   {"task_form": form, "tareas": _tareas})


def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    _tareas = Tareas.objects.all()
    print(_tareas)
    return render(request, "index.html", {"task_form": form, "tareas": _tareas})


def update_task(request, pk):
    task = Tareas.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update.html", {"task_edit_form": form})


# regiter user


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)

    # login user
def login_page(request):
    context = {}
    return render(request, 'login.html', context)

