from django.contrib import admin

from .models import Driver,Manager,Dispatcher,Servicer,Customer,Personnel
# Register your models here.

admin.site.register(Driver)
admin.site.register(Manager)
admin.site.register(Dispatcher)
admin.site.register(Servicer)
admin.site.register(Customer)
admin.site.register(Personnel)