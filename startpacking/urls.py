from django.contrib import admin
from django.urls import path, include, path
from packinglist import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_packing_list, name='get_packing_list'),
    path('add/', views.add_packing_list, name='add_packing_list'),
    path('add_task/', views.add_task, name='add_task')
]
