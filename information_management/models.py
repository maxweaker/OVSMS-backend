from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Chat(models.Model):
    content = models.TextField()
    customer = models.ForeignKey(to='man_management.Customer',on_delete=models.CASCADE)
    servicer = models.ForeignKey(to='man_management.Servicer',on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    from_serv = models.BooleanField(default=False)
    isEnding = models.BooleanField(default=False)
    def __str__(self):
        return self.content

class Notification(models.Model):
    content = models.TextField()
    publisher = models.ForeignKey(to='man_management.Dispatcher',on_delete=models.CASCADE)
    createTime = models.DateTimeField(default=timezone.now)
    updateTime = models.DateTimeField(default=timezone.now)

class ServingList(models.Model):
    servicer = models.ForeignKey(to='man_management.Servicer',on_delete=models.CASCADE)
    customer = models.ForeignKey(to='man_management.Customer',on_delete=models.CASCADE)
