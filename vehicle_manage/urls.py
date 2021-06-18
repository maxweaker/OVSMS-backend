from django.urls import path

from . import views

app_name = 'vehicle_manage'

urlpatterns = [
    path('vehicles', views.vehicles, name='vehicles'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
]