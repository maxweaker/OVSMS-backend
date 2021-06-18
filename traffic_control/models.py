from django.db import models
import datetime
import django.utils.timezone as timezone

#from man_management.models import Customer,Driver
# Create your models here.
class Car(models.Model):
    carModel = models.CharField(max_length=64)
    load = models.PositiveIntegerField()
    usable = models.BooleanField(default=True)
    remark = models.TextField()
    num = models.CharField(max_length=64,default="null")

    def __str__(self):
        return self.carModel

class Line(models.Model):
    lineName = models.CharField(max_length=64)
    length = models.PositiveIntegerField(default=0)
    userable = models.BooleanField(default=True)
    description = models.TextField(default='description')
    def __str__(self):
        return self.lineName

class Stop(models.Model):
    stopName = models.CharField(max_length=255)
    line = models.ForeignKey(Line,on_delete=models.CASCADE,related_name='line')
    sequence = models.PositiveIntegerField()

    def __str__(self):
        return self.stopName

class Frequency(models.Model):
    line = models.ForeignKey(Line,on_delete=models.CASCADE,related_name='frequency_line')
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='frequency_car')
    driver = models.ForeignKey(to='man_management.Driver',on_delete=models.CASCADE,
                               related_name='frequency_driver',default=1)

    departureTime = models.DateTimeField(default=timezone.now)
    arrivalTime = models.DateTimeField(default=timezone.now)
    remark = models.TextField(blank=True,default='')
    number = models.CharField(max_length=64,unique=True,default='xxx')
    reservation = models.IntegerField(default=0)

class RideRecord(models.Model):
    customer = models.ForeignKey(to='man_management.Customer',on_delete=models.CASCADE)
    frequency = models.ForeignKey(Frequency,on_delete=models.CASCADE)
    time = models.DateField(default=timezone.now)