from django import forms
from django.forms.models import inlineformset_factory
from .models import PackingList, Task


class PackingListForm(forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ['title']

# TaskForm is used for creating and updating tasks in the packing list.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed', 'packing_list']

# TaskFormSet is an inline formset used for handling multiple tasks in the packing list form.
# It allows users to add or remove tasks when creating or updating a packing list.
TaskFormSet = forms.inlineformset_factory(
    PackingList, Task, form=TaskForm, extra=0)