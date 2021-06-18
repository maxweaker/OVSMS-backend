from django.urls import path

from . import views

app_name = 'Chat'

urlpatterns = [
    path('send', views.send, name='vehicles'),
    path('getmessageList',views.getmessageList,name='getmessageList'),
    path('load_chatter', views.load_chatter, name='load_chatter'),
    path('end_com', views.end, name='end_com'),
]