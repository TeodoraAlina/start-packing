from django.test import TestCase
from .forms import PackingListForm, TaskForm, TaskFormSet
from .models import PackingList, Task

class FormsTest(TestCase):
    def test_packing_list_form_valid_data(self):
        form_data = {'title': 'Vacation Packing List'}
        form = PackingListForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_packing_list_form_blank_data(self):
        form_data = {'title': ''}
        form = PackingListForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_form_valid_data(self):
        packing_list = PackingList.objects.create(title='Vacation Packing List')
        form_data = {'title': 'Buy sunscreen', 'completed': False, 'packing_list': packing_list.id}
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_blank_data(self):
        form_data = {'title': '', 'completed': False, 'packing_list': None}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_formset_valid_data(self):
        packing_list = PackingList.objects.create(title='Vacation Packing List')
        Task.objects.create(title='Buy sunscreen', completed=False, packing_list=packing_list)
        Task.objects.create(title='Pack swimsuit', completed=True, packing_list=packing_list)

        form_data = {
            'task_set-TOTAL_FORMS': '2',
            'task_set-INITIAL_FORMS': '2',
            'task_set-0-id': '1',
            'task_set-0-title': 'Buy sunscreen',
            'task_set-0-completed': False,
            'task_set-0-packing_list': packing_list.id,
            'task_set-1-id': '2',
            'task_set-1-title': 'Pack swimsuit',
            'task_set-1-completed': True,
            'task_set-1-packing_list': packing_list.id,
        }

        formset = TaskFormSet(data=form_data, instance=packing_list)
        self.assertTrue(formset.is_valid())

    def test_task_formset_blank_data(self):
        form_data = {
            'task_set-TOTAL_FORMS': '1',
            'task_set-INITIAL_FORMS': '0',
            'task_set-0-title': '',
            'task_set-0-completed': False,
            'task_set-0-packing_list': None,
        }

        formset = TaskFormSet(data=form_data)
        self.assertFalse(formset.is_valid())