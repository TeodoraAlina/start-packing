from django.contrib import admin
from .models import PackingList
from .models import Task


admin.site.register(PackingList)
admin.site.register(Task)
