# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone


from NewsApp.models import News

def index(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    content = {
        'News' : news
        # 'Sales' : sale
    }
    return render(request, 'NewsApp/News.html', content)

class HomePageView(TemplateView):

    template_name = "project/home.html"

class AgreePageView(TemplateView):

    template_name = "project/agree.html"