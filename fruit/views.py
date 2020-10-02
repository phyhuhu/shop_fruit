from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages
import requests, json, datetime

from .models import CreateQModel
from .forms import QForm, TaskForm

from django_q.tasks import async_task, result, schedule, Task
from django_q.models import Schedule, OrmQ
from django_q.humanhash import humanize

# Create your views here.

def home(request):

    queue_orders = OrmQ.objects.all().order_by('lock')

    complete_orders = Task.objects.all().filter(
        func__exact='fruit.tasks.order_fruit',
        )
    
    content={
        'tableq': queue_orders,
        'tables': complete_orders
    }

    return render(request, 'fruit/home.html', content)

def createQ(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # form.save()
            fruit = form.cleaned_data.get('fruit')
            quantity = form.cleaned_data.get('quantity')
            create_time = form.cleaned_data.get('create_time')

            task_id = async_task(
                'fruit.tasks.order_fruit',
                fruit = fruit,
                quantity = quantity
                )

            messages.info(request, f'Task has been sent in queue.')
            return redirect('queue')
    else:
        form = TaskForm()

    content = {
        'form': form,
        }

    return render(request, 'fruit/createqueue.html', content)

def createS(request):
    if request.method == 'POST':
        form = QForm(request.POST)
        if form.is_valid():
            # form.save()
            task_name = form.cleaned_data.get('task_name')
            fruit = form.cleaned_data.get('fruit')
            quantity = form.cleaned_data.get('quantity')
            repeats = form.cleaned_data.get('repeats')
            schedule_type = form.cleaned_data.get('schedule_type')
            schedule_quantity = form.cleaned_data.get('schedule_quantity')
            start_time = form.cleaned_data.get('start_time')

            Schedule.objects.create(
                name=task_name,
                func='fruit.tasks.order_fruit',
                kwargs={'fruit':fruit,'quantity':quantity},
                schedule_type=Schedule.MINUTES,
                minutes=1,
                repeats=repeats,
                next_run=start_time
                )

            messages.info(request, f'Task "{task_name}" has been scheduled.')
            return redirect('schedule')
    else:
        form = QForm()

    content = {
        'form': form,
        }

    return render(request, 'fruit/createschedule.html', content)