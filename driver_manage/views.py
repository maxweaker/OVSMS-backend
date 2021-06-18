from django.shortcuts import render
import simplejson
from django.http import JsonResponse
from man_management.models import Driver
# Create your views here.

from django.http import Http404,HttpResponse

def driver_trans(driver):
    dict = {}
    dict['name'] = driver.name
    dict['num'] = driver.number
    dict['part'] = driver.isPartTime
    dict['avl'] = driver.isSuspened
    dict['age'] = driver.age
    return dict

def drivers(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        userType = r['userType']
        #if userType in ['调度员','人事']:
        driver_list = []
        drivers = Driver.objects.all()
        for driver in drivers:
            driver_list.append(driver_trans(driver))
        return JsonResponse({"drivers":driver_list})
        #return HttpResponse(status=404)

def add(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '人事':
            newDriver = r['newDriver']
            num = newDriver['num']
            driver = Driver.objects.filter(number=num)
            if driver.count() != 0:
                dict['success'] = False
            else:
                Driver.objects.create(number=newDriver['num'],isPartTime=newDriver['part'],
                                    isSuspened=newDriver['avl'],age=newDriver['age'],name=newDriver['name'])
        else:
            dict['success'] = False
    return JsonResponse(dict)

def edit(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '人事':
            newDriver = r['newDriver']
            num = newDriver['num']
            driver = Driver.objects.filter(number=num)
            if driver.count() != 1:
                dict['success'] = False
            else:
                driver.delete()
                Driver.objects.create(number=newDriver['num'],isPartTime=newDriver['part'],
                                    isSuspened=newDriver['avl'],age=newDriver['age'],name=newDriver['name'])
        else:
            dict['success'] = False
    return JsonResponse(dict)

def delete(request):
    if request.method == 'POST':
        dict = {"success": True}
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '人事':
            driver = Driver.objects.filter(number = r['num'])
            if driver.count() == 1:
                driver.delete()
            else:
                dict['success'] = False
        else:
            dict['success'] = False
        return JsonResponse(dict)