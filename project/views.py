# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

def index(request):
	# content = {
	# 	'Clients' : client,
	# 	'Sales' : sale
	# }
	return render(request, 'project/base.html')