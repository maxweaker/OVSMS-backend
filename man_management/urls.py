from django.urls import path

from . import views

app_name = 'man_management'

urlpatterns = [
    path('Register', views.register, name='register'),
    path('Login', views.login, name='login'),
]