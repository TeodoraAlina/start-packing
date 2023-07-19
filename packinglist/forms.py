from django import forms
from .models import PackingList
from .models import Task


class PackingListForm(forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ['title']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed', 'packing_list']
