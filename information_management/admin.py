from django.contrib import admin
# Register your models here.
from .models import Chat,Notification

admin.site.register(Chat)
admin.site.register(Notification)