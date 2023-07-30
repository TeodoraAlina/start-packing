from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import PackingList, Task
from .forms import PackingListForm, TaskFormSet


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_get_homepage(self):
        response = self.client.get(reverse('get_homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_packing_list(self):
        response = self.client.get(reverse('get_packing_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packinglist/packinglist.html')

    def test_add_packing_list(self):
        response = self.client.post(reverse('add_packing_list'), {
                                    'title': 'New Packing List'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PackingList.objects.count(), 1)

    def test_add_task(self):
        packing_list = PackingList.objects.create(
            user=self.user, title='Test Packing List')
        response = self.client.post(reverse('add_task'), {
            'title': 'New Task', 'packing_list': packing_list.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

    def test_edit_packing_list(self):
        packing_list = PackingList.objects.create(
            user=self.user, title='Test Packing List')
        response = self.client.get(
            reverse('edit_packing_list', args=[packing_list.id]))
        self.assertEqual(response.status_code, 200)

    def test_toggle_task(self):
        task = Task.objects.create(title='Test Task', packing_list=PackingList.objects.create(
            user=self.user, title='Test Packing List'))
        response = self.client.get(reverse('toggle_task', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_delete_item(self):
        task = Task.objects.create(title='Test Task', packing_list=PackingList.objects.create(
            user=self.user, title='Test Packing List'))
        response = self.client.get(
            reverse('delete_item', args=['task', task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
