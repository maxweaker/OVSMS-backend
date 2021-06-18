from django.shortcuts import render
from traffic_control.models import Car
import simplejson
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def car_trans(car):
    dict = {}
    dict['num'] = car.num
    dict['type'] = car.carModel
    dict['load'] = car.load
    dict['other'] = car.remark
    dict['avl'] = car.usable
    return dict

def vehicles(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        userType = r['userType']
        #if userType in ['管理员','调度员']:
        cars = Car.objects.all()
        formed_cars = []
        for car in cars:
            formed_cars.append(car_trans(car))
        return JsonResponse({"vehicles":formed_cars})
    else:
        return JsonResponse({})

def add(request):
    dict = {"success": True}
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '管理员':
            newVehicle = r['newVehicle']
            car = Car.objects.filter(num=newVehicle['num'])
            if car.count() == 1:
                dict['success'] = False
            else:
                Car.objects.create(num=newVehicle['num'],carModel=newVehicle['type'],load=newVehicle['load'],
                               usable=newVehicle['avl'],remark=newVehicle['other'])
    else:
        dict['success'] = False
    return JsonResponse(dict)

def delete(request):
    dict = {"success": True}
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '管理员':
            car = Car.objects.filter(num = r['num'])
            if car.count() == 1:
                car.delete()
            else:
                dict['success'] = False
        else:
            dict['success'] = False
        return JsonResponse(dict)
    else:
        return JsonResponse({})

def edit(request):
    dict = {"success": True}
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '管理员':
            newVehicle = r['newVehicle']
            car = Car.objects.filter(num=newVehicle['num'])
            if car.count() == 0:
                dict['success'] = False
            else:
                car.delete()
                Car.objects.create(num=newVehicle['num'],carModel=newVehicle['type'],load=newVehicle['load'],
                               usable=newVehicle['avl'],remark=newVehicle['other'])
    else:
        dict['success'] = False
    return JsonResponse(dict)