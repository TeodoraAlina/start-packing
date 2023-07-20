from __future__ import print_function
from django.shortcuts import render, redirect
from .models import PackingList
from .models import Task
from .forms import PackingListForm
from .forms import TaskForm


def get_packing_list(request):
    packinglists = PackingList.objects.all()
    tasks = Task.objects.all()
    context = {
        'packinglists': packinglists,
        'tasks': tasks
    }
    return render(request, 'packinglist/packinglist.html', context)


def add_packing_list(request):
    if request.method == 'POST':
        form = PackingListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_packing_list')
    else:
        form = PackingListForm()
    context = {
        'form': form
    }
    return render(request, 'packinglist/add_packinglist.html', context)


def add_task(request):
    if request.method == 'POST':
        form_task = TaskForm(request.POST)
        if form_task.is_valid():
            form_task.save()
            return redirect('get_packing_list')
    else:
        packing_list_id = request.GET.get('packing_list_id')
        form_task = TaskForm(initial={'packing_list': packing_list_id})
    context = {
        'form_task': form_task
    }
    return render(request, 'packinglist/add_task.html', context)

