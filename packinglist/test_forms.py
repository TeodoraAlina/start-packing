from django.test import TestCase
from django.contrib.auth.models import User
from .models import PackingList, Task
from .forms import PackingListForm, TaskForm, TaskFormSet


class FormsTest(TestCase):

    def test_packing_list_form_valid_data(self):
        form_data = {'title': 'Test Packing List'}
        form = PackingListForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_valid_data(self):
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        packing_list = PackingList.objects.create(
            user=user, title='Test Packing List')
        form_data = {
            'title': 'Test Task',
            'completed': False,
            'packing_list': packing_list.id
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_formset_empty_data(self):
        # Test formset with empty data, should be invalid.
        formset_data = {}
        formset = TaskFormSet(data=formset_data)
        self.assertFalse(formset.is_valid())

    def test_task_formset_invalid_data(self):
        # Test formset with invalid data, should be invalid.
        formset_data = {
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-MIN_NUM_FORMS': '0',
            'form-MAX_NUM_FORMS': '1000',
            # Missing 'form-0-title' field
            'form-0-completed': False,
            'form-0-packing_list': 1,
        }
        formset = TaskFormSet(data=formset_data)
        self.assertFalse(formset.is_valid())
