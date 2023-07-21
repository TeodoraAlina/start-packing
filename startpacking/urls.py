from django.contrib import admin
from django.urls import path, include, path
from packinglist import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_packing_list, name='get_packing_list'),
    path('add/', views.add_packing_list, name='add_packing_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_packing_list/<int:packing_list_id>/',
         views.edit_packing_list, name='edit_packing_list'),
    path('toggle_task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete_item/<str:item_type>/<int:item_id>/',
         views.delete_item, name='delete_item')
]
