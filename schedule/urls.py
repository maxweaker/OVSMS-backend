from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    path('serving', views.serving, name='serving'),
    path('history', views.history, name='history'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
]