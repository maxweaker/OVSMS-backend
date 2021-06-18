from django.urls import path

from . import views

app_name = 'traffic_control'

urlpatterns = [
    path('car_register', views.carRegister, name='car_register'),
    path('modify_stop', views.modifyStop, name='modify_stop'),
    path('ride_record',views.showRideRecord,name = 'show_record'),
    path('frequencies', views.showFrequency, name='show_frequencies')

]