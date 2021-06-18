from django.shortcuts import render
from .models import Customer,Dispatcher,Servicer,Manager,Driver,Personnel
import simplejson
from django.http import JsonResponse
# Create your views here.


def register(request):
    if request.method == 'POST':
        dict = {'success':True}
        r = simplejson.loads(request.body)
        new_username = r['username']
        new_password = r['password']

        test_name = Customer.objects.filter(name=new_username)

        if test_name.count() != 0:
            dict['success'] = False
            return JsonResponse(dict)

        else:
            new_cus = Customer()
            new_cus.name = new_username
            new_cus.password = new_password
            new_cus.age = 20
            new_cus.save()
            return JsonResponse(dict)
    else:
        return JsonResponse({})

def login(request):
    context = {"success": True, "userType": "None"}
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        username = r['username']
        password = r['password']
        cus = Customer.objects.filter(name = username)
        diver = Driver.objects.filter(name = username)
        serv = Servicer.objects.filter(name= username)
        disp = Dispatcher.objects.filter(name = username)
        mana = Manager.objects.filter(name = username)
        per = Personnel.objects.filter(name=username)
        #success是是否成功，userType有“管理员”“人事”“客户”“调度员” “服务员”
        if cus.count() == 1:
            context['userType'] = '客户'
            if Customer.objects.filter(name = username,password = password).count() == 0:
                context['success'] = False
        elif diver.count() == 1:
            context['userType'] = '司机'
            if Driver.objects.filter(name = username,password = password).count() == 0:
                context['success'] = False
        elif serv.count() == 1:
            context['userType'] = '服务员'
            if Servicer.objects.filter(name = username,password = password).count() == 0:
                context['success'] = False
        elif disp.count() == 1:
            context['userType'] = '调度员'
            if Dispatcher.objects.filter(name = username,password = password).count() == 0:
                context['success'] = False
        elif mana.count() == 1:
            if Manager.objects.filter(name = username,password = password).count() == 0:
                context['success'] = False
            context['userType'] = '管理员'
        elif per.count() == 1:
            if Personnel.objects.filter(name = username,password = password).count() == 0:
                context['success'] = False
            context['userType'] = '人事'
        else:
            context['success'] = False
        return JsonResponse(context)

    else:
        return JsonResponse({})