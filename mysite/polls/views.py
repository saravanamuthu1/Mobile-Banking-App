from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NameForm
import requests
import json
import time
from .models import apidata,money
from datetime import date
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from django.contrib import messages
# Create your views here.


def search_view(request):
    if 'q'in request.GET:
        q=request.GET['q']
        data=apidata.objects.filter(code__icontains=q)
    else:
        data=apidata.objects.all().distinct()
    context={
        'data':data
    }
    return render(request,'polls/forms.html',context)
def exchange_view(request):
    data=apidata.objects.all().distinct()
    result=""
    currency_from=''
    currency_to=''
    amount=''
    if request.method == "POST":
        amount = float(request.POST.get('amount'))
        currency_from = request.POST.get("cur_label")
        currency_to = request.POST.get("exchange_label")
        result = amount*float(currency_to)
    context={
        'data':data,
        'result':result,
        'amount':amount,
        'currency_from':currency_from,
        'currency_to':currency_to    
    }
    return render(request,'polls/base.html', context)
def stock_view(request):
    today=date.today()
    balance_amount=money.objects.all()
    context={
        'date':today,
        'balance_amount':balance_amount[0],
        'request':request,
    }
    return render(request,'polls/Pay.html',context)
def request_view(request):
    email=''
    message=""
    title="request money"
    if request.method == 'POST':
        email=request.POST.get("email")
        message=request.POST.get("message")
        try:  
            send_mail(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return HttpResponseRedirect("/stocks/")
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request,'polls/requestmoney.html')
def sendmoney_view(request):
    message="A deposit has occure"
    title="deposit message"
    if request.method == 'POST':
        email=request.POST.get('email')
        amount=request.POST.get('amount')
        present_balance=money.objects.all()
        value=present_balance[0].balance
        cur_balance=int(amount)-int(value)
        message="A deposit of" + " " + "$"+ amount + " " + "has been credited to your account"
        money.objects.update(balance=cur_balance)
        try:  
            send_mail(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return HttpResponseRedirect("/stocks/")
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request,'polls/sendmoney.html')
def nav_active(request):
    context={
        'request':request,
    }
    return render(request,'polls/navbar.html',context)