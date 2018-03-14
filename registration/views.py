# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import LoginForm


def index(request):
    print("index")
    return render(request, 'registration/index.html')

# def login(request):
#     if ('username' in request.REQUEST) and ('password' in request.REQUEST):
#         username = request.REQUEST['username']
#         password = request.REQUEST['password']
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#     		login(request, user)
#     return renderrender(request, 'registration/index.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return HttpResponseRedirect("/welcome")# Redirect to a success page.
#         return HttpResponseRedirect("/login")
#     form=LoginForm()
#     return render(request, 'registration/index.html', {'login_form': LoginForm})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/polls")# Redirect to a success page.
        print("not")
    # else:
    #     form.add_error(None, 'Ошибка авторизации')
    #     return render(request, 'registration/index.html',{'login_form': form})
    return render(request, 'registration/index.html', {'login_form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/polls")

def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/polls")
        else: 
            print('Error')
    else:
        data, errors = {}, {}
    return render(request, 'registration/reg.html',{'form': form})