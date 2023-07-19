from django.shortcuts import render, redirect
from .models import PackingList
from .models import Task
from .forms import PackingListForm


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
    form = PackingListForm()
    context = {
        'form': form
    }
    return render(request, 'packinglist/add_packinglist.html', context)

