from django.shortcuts import render
from .models import PackingList
from .models import Task


def get_packing_list(request):
    packinglists = PackingList.objects.all()
    tasks = Task.objects.all()
    context = {
        'packinglists': packinglists,
        'tasks': tasks
    }
    return render(request, 'packinglist/packinglist.html', context)


def add_packing_list(request):
    return render(request, 'packinglist/add_packinglist.html')
