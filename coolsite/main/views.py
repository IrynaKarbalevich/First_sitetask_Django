from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create_task(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = AddForm()
    return render(request, 'main/create.html', {'title': "Добавление задачи", 'form': form})
