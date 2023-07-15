from django.shortcuts import render
from .models import PackingList
from .models import Task


def get_packing_list(request):
    packinglists = PackingList.objects.all()
    context = {
        'packinglists': packinglists
    }
    return render(request, 'packinglist.html', context)
