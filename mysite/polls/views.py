from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NameForm
import requests
import json
import time
from .models import apidata
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