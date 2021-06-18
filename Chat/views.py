from django.shortcuts import render

from man_management.models import Customer,Servicer,Dispatcher
from information_management.models import Chat,ServingList,Notification
import simplejson
from django.http import JsonResponse
import django.utils.timezone
import datetime
# Create your views here.

def send(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        print(r)
        from_serv = r['type']
        content = r['content']
        print(r)
        if from_serv == True:
            serv = Servicer.objects.get(name=r['Fromid'])
            cus = Customer.objects.get(name=r['Toid'])
        else:
            cus = Customer.objects.get(name=r['Fromid'])
            serv = Servicer.objects.get(name=r['Toid'])
        Chat.objects.create(customer=cus,servicer=serv,from_serv=from_serv,content=r['content'],
                            time=django.utils.timezone.now()+datetime.timedelta(hours=8))
    return JsonResponse({"success":True})

def chat_trans(chat):
    dict = {}
    dict['type'] = chat.from_serv
    dict['time'] = chat.time
    dict['content'] = chat.content
    dict['isEnd'] = chat.isEnding
    return dict

def getmessageList(request):
    if request.method == 'POST':
        dict = {"success":True}

        r = simplejson.loads(request.body)
        print(r)
        chat_list = []
        cus = Customer.objects.get(name=r['cid'])
        serv = Servicer.objects.get(name=r['sid'])
        chats = Chat.objects.filter(servicer=serv,customer=cus).order_by('time')
        for chat in chats:
            chat_list.append(chat_trans(chat))
        return JsonResponse({"messageList":chat_list})

def load_chatter(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        ToList = []
        if r['isService'] == False:
            cus = Customer.objects.get(name=r['Fromid'])
            svlist = ServingList.objects.filter(customer=cus)
            print(svlist)

            if svlist.count() != 0:
                for sv in svlist:
                    ToList.append({"Toid":sv.servicer.name})
                pass
            else:
                servs = Servicer.objects.all().order_by('servingNum')
                for serv in servs:
                    ServingList.objects.create(servicer=serv,customer=cus)
                    ToList.append({"Toid":serv.name})
                    serv.servingNum = serv.servingNum + 1
                    serv.save()
                    break
        else:
            serv = Servicer.objects.get(name=r['Fromid'])
            servLists = ServingList.objects.filter(servicer=serv)
            cus = customers = []
            for s in servLists:
                customers.append(s.customer)
            print(customers)
            for cus in customers:
                ToList.append({"Toid": cus.name})

        return JsonResponse({"ToList":ToList})

def end(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        print(r)
        try:
            cus = Customer.objects.get(name=r['cid'])
            serv = Servicer.objects.get(name=r['sid'])
            Chat.objects.create(customer=cus,servicer=serv,isEnding=True,content="END",
                                time=django.utils.timezone.now()+datetime.timedelta(hours=8))
            ServingList.objects.get(customer=cus,servicer=serv).delete()
            serv.servingNum = serv.servingNum - 1
            serv.save()
        except :
            dict['success'] = False
    return JsonResponse(dict)

def send_noti(request):
    if request.method == 'POST':
        dict = {"success":True}
        r = simplejson.loads(request.body)
        userType = r['userType']
        if userType in ['调度员']:
            notify = r['notify']
            content = r['content']
            disp = Dispatcher.objects.get(number=r['number'])
            Notification.objects.create(content=content,publisher=disp,
                                        createTime=django.utils.timezone.now()+datetime.timedelta(hours=8))
    return JsonResponse({})