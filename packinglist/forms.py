from django import forms
from .models import PackingList


class PackingListForm(forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ['title']
