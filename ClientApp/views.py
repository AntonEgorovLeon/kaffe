from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic

from .models import Client

def index(request):
	return render(request, 'ClientApp/Client.html')

class IndexView(generic.ListView):
    model = Client
    template_name = 'ClientApp/indexClient.html'
    context_object_name = 'clients'
