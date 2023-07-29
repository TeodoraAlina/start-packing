from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import PackingList, Task
from .forms import PackingListForm, TaskForm, TaskFormSet


def get_homepage(request):
    return render(request, 'index.html')


@login_required
def get_packing_list(request):
    packinglists = PackingList.objects.filter(user=request.user)
    tasks = Task.objects.filter(packing_list__user=request.user)
    context = {
        'packinglists': packinglists,
        'tasks': tasks
    }
    return render(request, 'packinglist/packinglist.html', context)


@login_required
def add_packing_list(request):
    if request.method == 'POST':
        form = PackingListForm(request.POST)
        if form.is_valid():
            packing_list = form.save(commit=False)
            packing_list.user = request.user
            packing_list.save()
            return redirect('get_packing_list')
    else:
        form = PackingListForm()
    context = {
        'form': form
    }
    return render(request, 'packinglist/add_packinglist.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form_task = TaskForm(request.POST)
        if form_task.is_valid():
            form_task.save()
            return redirect('get_packing_list')
    else:
        packing_list_id = request.GET.get('packing_list_id')
        if packing_list_id is None:
            return redirect('get_packing_list')

        form_task = TaskForm(initial={'packing_list': packing_list_id})
    context = {
        'form_task': form_task
    }
    return render(request, 'packinglist/add_task.html', context)


@login_required
def edit_packing_list(request, packing_list_id):
    packing_list = get_object_or_404(
        PackingList, id=packing_list_id, user=request.user)
    tasks = Task.objects.filter(packing_list=packing_list)

    if request.method == 'POST':
        packing_list_form = PackingListForm(
            request.POST, instance=packing_list)
        task_formset = TaskFormSet(request.POST, instance=packing_list)

        if packing_list_form.is_valid() and task_formset.is_valid():
            packing_list_form.save()
            task_formset.save()
            return redirect('get_packing_list')
    else:
        packing_list_form = PackingListForm(instance=packing_list)
        task_formset = TaskFormSet(instance=packing_list)

    context = {
        'packing_list': packing_list,
        'tasks': tasks,
        'packing_list_form': packing_list_form,
        'task_formset': task_formset
    }
    return render(request, 'packinglist/edit_packinglist.html', context)


@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, packing_list__user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('get_packing_list')


@login_required
def delete_item(request, item_type, item_id):
    model = None
    if item_type == 'task':
        model = Task
    elif item_type == 'packinglist':
        model = PackingList

    if model:
        item = get_object_or_404(model, id=item_id)
        item.delete()

    return redirect('get_packing_list')
