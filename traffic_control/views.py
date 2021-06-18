from django.shortcuts import render
from .models import Car,Stop,RideRecord,Frequency
from man_management.models import Customer
# Create your views here.
def carRegister(request):
    if request.method == 'POST':
        new_carModel = request.POST.get('carModel')
        new_load = request.POST.get('load')
        new_usable = request.POST.get('usable')
        new_remark = request.POST.get('remark')
        try:
            Car.objects.create(carModel=new_carModel,load=new_load,
                               usable=new_usable,remark=new_remark)
            return render(request, 'car_register.html', {'message': '车辆注册成功！'})
        except :
            return HttpResponse('失败')
    if request.method == 'GET':
        return render(request, 'car_register.html', {'message': '输入车辆信息'})


def modifyStop(request):

    if request.method == 'POST':
        stopName = request.POST.get('stopName')
        lineID = request.POST.get('line_id')
        if request.POST.get('pattern') == 'delete':
            stop = Stop.objects.get(stopName=stopName, line_id=lineID)
            line = stop.line
            line.length = line.length - 1
            line.save()
            current_sequence = stop.sequence
            nextStops = Stop.objects.filter(line_id=lineID,sequence__gt = current_sequence)
            stop.delete()
            for stop in nextStops:
                stop.sequence = stop.sequence - 1
                stop.save()
            return render(request,'modify_stop.html',{'message':'删除成功'})

        elif request.POST.get('pattern') == 'create':
            input_sequence = request.POST.get('sequence')
            aheadStops = Stop.objects.filter(line_id=lineID,sequence__gte = input_sequence)
            for stop in aheadStops:
                stop.sequence = stop.sequence + 1
                stop.save()
            newStop = Stop.objects.create(stopName=stopName,line_id=lineID,sequence=input_sequence)
            line = newStop.line
            line.length = line.length + 1
            line.save()
            return render(request, 'modify_stop.html', {'message': '添加成功'})

def showRideRecord(request):
    if request.method == 'GET':
        request.session['username'] = '张三'
        cus_name = request.session['username']
        cus = Customer.objects.get(name=cus_name)
        record = RideRecord.objects.filter(customer_id = cus.id)
        return render(request,'ride_record.html',{'record':record})

def showFrequency(request):
    if request.method == 'GET':
        frequencies = Frequency.objects.all()
        return render(request,'frequencys.html',{'frequencies':frequencies})

