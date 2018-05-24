# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import SaleForm, ClientForm
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from ClientApp.models import Client
from .models import Sale, Good
from django.db import connection

# Create your views here.
#-*- coding:utf-8 -*-

@login_required(login_url='/registration/login/')
def index(request):
    form = SaleForm(request.POST)
    client = Client.objects.all()
    if request.method == "POST":
        if form.is_valid():
            sale = form.save(commit=False)
            sale.Date = timezone.now()
            me = request.user
            sale.id_manager = me
            # id_client from POST is not a model object (just string of client name)
            # it needs to be replaced by an object in sale.form
            sale.id_client = Client.objects.get(ShortName=request.POST.get('id_client'))
            if sale.id_client.pk == 20: 
                f1 = False
            else:
                f1 = True
            if Sale.objects.filter(id_client=sale.id_client, Date=sale.Date, id_product=sale.id_product).exists() and f1:
                sale.save()
                form.add_error(None, 'Такой посетитель уже учтен')
                return render(request, 'ShopApp/manager.html',{'form': form,'Clients': client})
            else:
                sale.save()
                form.add_error(None, 'Продажа учтена')
                return render(request, 'ShopApp/manager.html',{'form': form,'Clients': client})
        else:
            form = SaleForm()
    return render(request, 'ShopApp/manager.html',{'form': form,'Clients': client})


@login_required(login_url='/registration/login/')
def charts(request):
    data = ClientForm(request.POST)
    return render(request, 'ShopApp/charts.html',{'clientForm': data})

def charts_get(request):
    date1=request.POST.get(u'id1')
    date2=request.POST.get(u'id2')
    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    with connection.cursor() as c:
        c.execute('select Date as date, count(id) as sales from ShopApp_sale where Date between \''+date1+'\' and \''+date2+'\' group by Date order by Date')
        return JsonResponse(dictfetchall(c), safe=False)
    return render(request, 'ShopApp/charts.html')


def client_record(request):
    wanted = request.POST.get('cl_id')
    sale = Sale.objects.filter(id_client=wanted).values('id_client__ShortName','Date','id_product__Name')
    # visit = Visit.objects.filter(id_client=wanted)
    # data = serializers.serialize('json', visit, fields('id_client','date','id_product'))
    # return JsonResponse(visit, safe=False)
    return JsonResponse({'listVal': list(sale)})

def client_auto(request):
    term = request.POST.get('keyword')
    listClients = Client.objects.filter(ShortName__icontains=term).values('ShortName','Site','Birthdate','id')
    return JsonResponse({'listVal':list(listClients)})

