"""OVSMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('man_management.urls')),
    path('schedule/',include('schedule.urls')),
    path('vehicle_manage/',include('vehicle_manage.urls')),
    path('line_manage/',include('line_manage.urls')),
    path('driver_manage/',include('driver_manage.urls')),
    path('Chat/',include('Chat.urls')),
    path('ride_record/',include('ride_record.urls')),
    path('api/',include('api_test.urls')),
    path('information_management/',include('information_management.urls')),
    path('',TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
]
