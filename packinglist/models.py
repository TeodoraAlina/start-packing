from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model for PackingList, representing a user's packing list for vacation
class PackingList(models.Model):
    # ForeignKey to User, indicating the user who owns this packing list
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False)
    # CharField for the title of the packing list
    title = models.CharField(max_length=70)
    # DateField to store the creation date of the packing list (default set to current time)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

# Model for Task, representing a task within a packing list
class Task(models.Model):
    # CharField for the title of the task
    title = models.CharField(max_length=200)
    # ForeignKey to PackingList, indicating the packing list to which this task belongs
    packing_list = models.ForeignKey(
        PackingList, on_delete=models.CASCADE, related_name="tasks")
    # DateField to store the creation date of the task (default set to current time)
    created_task_date = models.DateField(default=timezone.now)
    # BooleanField to indicate whether the task is completed or not (default set to False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # Class Meta to specify the ordering of tasks based on their completed status
    class Meta:
        ordering = ['completed']