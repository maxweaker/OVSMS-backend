from django.urls import path

from . import views

app_name = 'ride_record'

urlpatterns = [
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('records', views.records, name='records'),
]