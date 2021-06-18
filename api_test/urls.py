from django.conf.urls import url, include
from api_test import views
from django.urls import path, include
urlpatterns = [
    path('test/',views.test),
    path('user/',views.ret_book),
]