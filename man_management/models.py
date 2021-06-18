from django.db import models
import django.utils.timezone
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
    def __str__(self):
        return self.name


class Customer(Person):
    startLine = models.ForeignKey(to='traffic_control.Line',on_delete=models.CASCADE,null=True,default=None,blank=True)

class Position(models.TextChoices):
    MANAGER = 'MN', 'Manager'
    DIVER = 'DV', 'Diver'
    SERVICER = 'SV','Servicer'
    DISPATCHER = 'DP','Dispatcher'
    PERSONNEL = 'PN','Personnel'

class Employee(Person):
    entranceTime = models.DateTimeField(auto_now_add=True)
    isSuspened = models.BooleanField(default=False)
    number = models.CharField(max_length=64, default="number")
    class Meta:
        abstract = True

class Driver(Employee):
    position = models.CharField(
        max_length=2,
        choices=Position.choices,
        default=Position.DIVER
    )
    number = models.CharField(max_length=64,default="number")
    isPartTime = models.BooleanField()
    car = models.ForeignKey(to='traffic_control.Car',on_delete=models.DO_NOTHING,null=True,default=None,blank=True)
    line = models.ForeignKey(to='traffic_control.Line',on_delete=models.DO_NOTHING,null=True,default=None,blank=True)

class Servicer(Employee):
    position = models.CharField(
        max_length=2,
        choices=Position.choices,
        default=Position.SERVICER
    )
    servingNum = models.IntegerField(default=0)

class Manager(Employee):
    position = models.CharField(
        max_length=2,
        choices=Position.choices,
        default=Position.MANAGER
    )

class Dispatcher(Employee):
    position = models.CharField(
        max_length=2,
        choices=Position.choices,
        default=Position.DISPATCHER
    )

class Personnel(Employee):
    position = models.CharField(
        max_length=2,
        choices=Position.choices,
        default=Position.PERSONNEL
    )