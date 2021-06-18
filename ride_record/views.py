from django.shortcuts import render
import simplejson
from django.http import JsonResponse
from traffic_control.models import Line,Frequency,Car,RideRecord
from man_management.models import Driver,Customer
import django.utils.timezone as tmz
import datetime
from schedule.views import freq_trans
# Create your views here.
def add(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        print(r)
        username = r['username']
        password = r['password']
        freqnum = r['id']
        try:
            cus = Customer.objects.get(name=username,password=password)
            frq = Frequency.objects.get(number=freqnum)
            ride = RideRecord.objects.filter(customer=cus,frequency=frq)
            if ride.count() == 0:
                RideRecord.objects.create(customer=cus,time=tmz.now(),frequency=frq)
                frq.reservation = frq.reservation + 1
                frq.save()
            else:
                dict['success'] = False
        except :
            dict['success'] = False
    return JsonResponse(dict)

def delete(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        print(r)
        username = r['username']
        password = r['password']
        freqnum = r['id']
        try:
            cus = Customer.objects.get(name=username, password=password)
            frq = Frequency.objects.get(number=freqnum)
            RideRecord.objects.get(customer=cus, frequency=frq).delete()
            frq.reservation = frq.reservation - 1
            frq.save()
        except :
            dict['success'] = False
    return JsonResponse(dict)

def records(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        cus = Customer.objects.get(name=r['username'])
        recods = RideRecord.objects.filter(customer=cus)
        freq_list = []
        for record in recods:
            freq_list.append(freq_trans(record.frequency))
        print(freq_list)
    return JsonResponse({"records":freq_list})
