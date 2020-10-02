from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Tareas

# Create your views here.
def lista_tareas(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    _tareas = Tareas.objects.all()
    print(_tareas)
    return render(request, "index.html",  {"tareas": _tareas})


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
