from django.shortcuts import render, redirect
from .models import *
from .forms import AddTask
from .forms import RegisterForm


def home(request):
    return render(request, 'home.html')


def index(request):
    if request.user.is_active:
        count = Task.objects.filter(author=request.user, completed=False).count
    else:
        count = Task.objects.all().count
    if request.user.is_active:
        task = Task.objects.filter(author=request.user).order_by('completed', '-created_on')
    else:
        task = Task.objects.all()
    form = AddTask()
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('/')
    return render(request, 'todolist.html', {'task': task, 'form': form, 'count': count})


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = AddTask(instance=task)
    if request.method == 'POST':
        form = AddTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'updatetask.html', {'form': form})


def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


def complete(request, pk):
    task = Task.objects.get(id=pk)
    if task.completed == False:
        task.completed = True
        task.save()
    else:
        task.completed = False
        task.save()
    return redirect('/')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'register.html', {'form': form})


def login(request):
    return render(request, 'login.html')
