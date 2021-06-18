from django.shortcuts import render
import simplejson
from django.http import JsonResponse
from traffic_control.models import Line,Stop
# Create your views here.
def line_trans(line):
    dict = {}
    dict['num'] = line.lineName
    dict['other'] = line.description
    dict['avl'] = line.userable
    l_pk = line.pk
    stops = Stop.objects.filter(line = l_pk).order_by('sequence')
    stop_list = []
    for stop in stops:
        s_dic = {}
        s_dic['name'] = stop.stopName
        stop_list.append(s_dic)
    dict['stops'] = stop_list
    return dict


def lines(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        userType = r['userType']
        #if userType in ['管理员','调度员']:
        line_list = []
        lines = Line.objects.all()
        for line in lines:
            line_list.append(line_trans(line))
        return JsonResponse({"lines":line_list})
    else:
        return JsonResponse({})

def create_stop(stops,line):
    count = 1;
    for stop in stops:
        Stop.objects.create(stopName=stop['name'],sequence=count,line=line)
        count = count + 1
    return

def add(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '管理员':
            newLine = r['newLine']
            lineName = newLine['num']
            line = Line.objects.filter(lineName=lineName)
            if line.count() != 0:
                dict['success'] = False
            else:
                stops = newLine['stops']
                line = Line.objects.create(lineName=lineName,length=len(stops),
                                    userable=newLine['avl'],description=newLine['other'])
                create_stop(stops,line)
        else:
            dict['success'] = False
    return JsonResponse(dict)

def edit(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        print(r)
        userType = r['userType']
        if userType == '管理员':
            newLine = r['newLine']
            lineName = newLine['num']
            line = Line.objects.filter(lineName=lineName)
            if line.count() != 1:
                dict['success'] = False
            else:
                line.delete()
                stops = newLine['stops']
                line = Line.objects.create(lineName=lineName,length=len(stops),
                                    userable=newLine['avl'],description=newLine['other'])
                create_stop(stops,line)
        else:
            dict['success'] = False
    return JsonResponse(dict)

def delete(request):
    if request.method == 'POST':
        dict = {"success": True}
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType == '管理员':
            line = Line.objects.filter(lineName = r['num'])
            if line.count() == 1:
                line.delete()
            else:
                dict['success'] = False
        else:
            dict['success'] = False
        return JsonResponse(dict)

