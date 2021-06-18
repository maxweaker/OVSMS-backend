from django.shortcuts import render
from .models import Chat,Notification
from man_management.models import Customer,Servicer
# Create your views here.
def showChatRecord(request):
    if request.method == 'GET':
        request.session['username'] = '张三'
        request.session['servicer_name'] = 'asdh'
        cus_name = request.session['username']
        sev_name = request.session['servicer_name']
        cus_id = Customer.objects.get(name=cus_name).id
        sev_id = Servicer.objects.get(name=sev_name).id

        records = Chat.objects.filter(customer_id = cus_id,servicer_id = sev_id)
        return render(request,'chat_record.html',{'records':records})