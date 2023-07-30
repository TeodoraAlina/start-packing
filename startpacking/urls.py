from django.contrib import admin
from django.urls import path, include, path
from packinglist import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.get_homepage, name='get_homepage'),
    path('packing_list', views.get_packing_list, name='get_packing_list'),
    path('add/', views.add_packing_list, name='add_packing_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_packing_list/<int:packing_list_id>/',
         views.edit_packing_list, name='edit_packing_list'),
    path('toggle_task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete_item/<str:item_type>/<int:item_id>/',
         views.delete_item, name='delete_item')
]

handler404 = views.custom_404
handler500 = views.custom_500
handler403 = views.custom_403
handler405 = views.custom_405
