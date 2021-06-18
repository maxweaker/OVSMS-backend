from django.urls import path

from . import views

app_name = 'information_management'

urlpatterns = [
    path('chat_record', views.showChatRecord, name='chat_record'),

]