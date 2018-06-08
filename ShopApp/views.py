# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import SaleForm, ClientForm, VisitForm
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
    products = Good.objects.all()
    if request.method == "POST":
        if form.is_valid():
            sale = form.save(commit=False)
            sale.Date = timezone.now()
            sale.id_manager = request.user
            # id_client from POST is not a model object (just string of client name)
            # it needs to be replaced by an object in sale.form
            sale.id_client = Client.objects.get(ShortName=request.POST.get('id_client'))
            sale.id_product = Good.objects.get(Name=request.POST.get('id_product'))
            good1 = sale.id_product
            if good1.FreeAmount < 1:
                form.add_error(None, 'Недостаточно товара')
                return render(request, 'ShopApp/manager.html',{'form': form,'Clients': client, 'Goods':products})
            else:
                good1.FreeAmount = good1.FreeAmount - 1
                good1.save()
                sale.save()
                form.add_error(None, 'Продажа учтена')
                return render(request, 'ShopApp/manager.html',{'form': form,'Clients': client, 'Goods':products})
        else:
            form = SaleForm()
    return render(request, 'ShopApp/manager.html',{'form': form,'Clients': client, 'Goods':products})


@login_required(login_url='/registration/login/')
def visit_add(request):
    form = VisitForm(request.POST)
    client = Client.objects.all()
    if request.method == "POST":
        if form.is_valid():
            visit = form.save(commit=False)
            visit.Date = timezone.now()
            visit.id_manager = request.user
            # id_client from POST is not a model object (just string of client name)
            # it needs to be replaced by an object in sale.form
            visit.id_client = Client.objects.get(ShortName=request.POST.get('id_client'))
            if visit.id_client.pk == 20: 
                f1 = False
            else:
                f1 = True
            if Sale.objects.filter(id_client=visit.id_client, Date=visit.Date).exists() and f1:
                visit.save()
                form.add_error(None, 'Такой посетитель уже учтен')
                return render(request, 'ShopApp/add_visit.html',{'form': form,'Clients': client})
            else:
                visit.save()
                form.add_error(None, 'Посетитель учтен')
                return render(request, 'ShopApp/add_visit.html',{'form': form,'Clients': client})
        else:
            form = VisitForm()
    return render(request, 'ShopApp/add_visit.html',{'form': form,'Clients': client})


@login_required(login_url='/registration/login/')
def charts(request):
    data = ClientForm(request.POST)
    return render(request, 'ShopApp/charts.html',{'clientForm': data})

def charts_get(request):
    date1=request.POST.get("id1")
    date2=request.POST.get('id2')
    dates=request.POST.getlist('dates[]')

    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    with connection.cursor() as c:
        # c.execute('select Date as date, count(id) as sales from ShopApp_sale where Date between \''+date1+'\' and \''+date2+'\' group by Date order by Date'%(date1, date2))
        c.execute('select "Date", count(id) as Visits from public."ShopApp_visit" where "Date" between \'%s\' and \'%s\' group by "Date" order by "Date"'%(date1, date2))
        return JsonResponse(dictfetchall(c), safe=False)
    return render(request, 'ShopApp/charts.html')

def charts_get1(request):
    date1=request.POST.get("id11")
    date2=request.POST.get('id12')

    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    print(date1)
    print(date2)
    with connection.cursor() as c:
        # c.execute('select Date as date, count(id) as sales from ShopApp_sale where Date between \''+date1+'\' and \''+date2+'\' group by Date order by Date'%(date1, date2))
        c.execute('select "Date", count(id) as sales from public."ShopApp_sale" where "Date" between \'%s\' and \'%s\' group by "Date" order by "Date"'%(date1, date2))
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

