from django.shortcuts import render
import simplejson
from django.http import JsonResponse
from traffic_control.models import Line,Frequency,Car
from man_management.models import Driver
import django.utils.timezone
import datetime
from django.db.models import Q
# Create your views here.

#{userType,newSchedule:{num,line,vehicle,driver,duration{
#start:{year,month,day,hour,minute}
#end:{year,month,day,hour,minute}
#},other}}

def time_trans(t):
    return str(t.year)+"/"+str(t.month).rjust(2,'0')+"/"+str(t.day).rjust(2,'0')+\
           " "+str(t.hour).rjust(2,'0')+":"+str(t.minute).rjust(2,'0')

def dict_to_time(dict):
    year = int(dict['year'])
    month = int(dict['month'])
    day= int(dict['day'])
    hour = int(dict['hour'])
    minute = int(dict['minute'])
    t = datetime.datetime(year,month,day,hour,minute)+datetime.timedelta(hours=8)
    return t

def freq_trans(freq):
    dict = {}
    dict['num'] = freq.number
    dict['line'] = freq.line.lineName
    dict['vehicle'] = freq.car.num
    dict['driver'] = freq.driver.number
    dict['start'] = time_trans(freq.departureTime)
    dict['end'] = time_trans(freq.arrivalTime)
    dict['reservation'] = freq.reservation
    dict['other'] = freq.remark
    return dict

def serving(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        userType = r['userType']
        schedules = []
        freqs = Frequency.objects.filter(arrivalTime__gt=django.utils.timezone.now()+datetime.timedelta(hours=8))
        allfreqs = Frequency.objects.all()
        for a in allfreqs:
            print(a.arrivalTime)
        print(django.utils.timezone.now()+datetime.timedelta(hours=8))
        freq_list = []
        for freq in freqs:
            freq_list.append(freq_trans(freq))
    return JsonResponse({"servings":freq_list})

def history(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        userType = r['userType']
        #if userType in ['管理员','调度员']:
        schedules = []
        freqs = Frequency.objects.filter(arrivalTime__lt=django.utils.timezone.now()+datetime.timedelta(hours=8))
        freq_list = []
        for freq in freqs:
            print(type(freq.arrivalTime))
            freq_list.append(freq_trans(freq))
    return JsonResponse({"servings":freq_list})


def add(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        print(r)
        userType = r['userType']
        if userType in ['调度员']:
            newSchedule = r['newSchedule']
            number = newSchedule['num']
            freq = Frequency.objects.filter(number=number)
            if freq.count() !=0:
                dict['success'] = False
            else:
                driver = Driver.objects.get(number=newSchedule['driver'])
                line = Line.objects.get(lineName=newSchedule['route'])
                car = Car.objects.get(num=newSchedule['vehicle'])
                remark = newSchedule['other']
                duration = newSchedule['duration']
                start = dict_to_time(duration['start'])
                end = dict_to_time(duration['end'])
                car_re_freq = Frequency.objects.filter(Q(car=car,departureTime__lte=start,arrivalTime__gte=start)
                                                        | Q(car=car,departureTime__lte=end,arrivalTime__gte=end))
                driver_re_freq = Frequency.objects.filter(Q(driver=driver,departureTime__lte=start,arrivalTime__gte=start)
                                                        | Q(driver=driver,departureTime__lte=end,arrivalTime__gte=end))
                if car_re_freq.count() != 0 or driver_re_freq.count() != 0:
                    dict['success'] = False
                else:
                    Frequency.objects.create(driver=driver,car=car,line=line,
                                             remark=remark,number=number,
                                             departureTime=start,arrivalTime=end)
        else:
            dict['success'] = False
        return JsonResponse(dict)

def delete(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType in ['调度员']:
            number = r['num']
            try:
                freq = Frequency.objects.get(number=number).delete()
            except:
                pass
                dict['success'] = False
        else:
            dict['success'] = False
    return JsonResponse(dict)