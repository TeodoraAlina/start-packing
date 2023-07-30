from django.test import TestCase
from django.contrib.auth.models import User
from .models import PackingList, Task
from django.utils import timezone


class PackingListModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a packing list object
        self.packing_list = PackingList.objects.create(
            user=self.user,
            title='Test Packing List',
        )

    def test_packing_list_creation(self):
        self.assertEqual(self.packing_list.title, 'Test Packing List')
        self.assertEqual(self.packing_list.user, self.user)
        self.assertIsNotNone(self.packing_list.created_date)

    def test_packing_list_str(self):
        self.assertEqual(str(self.packing_list), 'Test Packing List')


class TaskModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a packing list object
        self.packing_list = PackingList.objects.create(
            user=self.user,
            title='Test Packing List',
        )

        # Create a task object
        self.task = Task.objects.create(
            title='Test Task',
            packing_list=self.packing_list,
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.packing_list, self.packing_list)
        self.assertIsNotNone(self.task.created_task_date)
        self.assertFalse(self.task.completed)

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_ordering(self):
        task2 = Task.objects.create(
            title='Another Task',
            packing_list=self.packing_list,
        )
        task3 = Task.objects.create(
            title='Yet Another Task',
            packing_list=self.packing_list,
            completed=True,
        )

        tasks = Task.objects.filter(packing_list=self.packing_list)
        self.assertEqual(list(tasks), [self.task, task2, task3])