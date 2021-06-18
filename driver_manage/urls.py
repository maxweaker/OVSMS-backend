from django.urls import path

from . import views

app_name = 'line_manage'

urlpatterns = [
    path('drivers', views.drivers, name='drivers'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
]