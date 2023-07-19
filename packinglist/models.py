from django.db import models
from django.contrib.auth.models import User


class PackingList(models.Model):
    title = models.CharField(max_length=70)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    packing_list = models.ForeignKey(PackingList, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
