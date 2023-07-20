from django import forms
from django.forms.models import inlineformset_factory
from .models import PackingList, Task


class PackingListForm(forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ['title']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed', 'packing_list']


TaskFormSet = forms.inlineformset_factory(
    PackingList, Task, form=TaskForm, extra=1)
