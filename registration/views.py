# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm,
    PasswordChangeForm
)
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, FormView, View
from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ClientApp.models import Client
from .models import (
    LoginForm, 
    RegistrationForm, 
    EditProfileForm, 
    ProfileForm
)

@login_required(login_url='/registration/login/')
def profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return render(request, 'registration/profile.html', context)
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'registration/profile.html', context)

@login_required(login_url='/registration/login/')
def profile_change(request):
    if request.method == 'POST':        
        client = Client.objects.get(user=request.user)
        form = ProfileForm(request.POST, instance=client)
        if form.is_valid():
            print(client.user.id)
            print(client.Phone)
            form.save()
            client.Phone = form.cleaned_data.get("Phone", None)
            client.save()
            context = {'form': form}
            # return render(request, 'registration/profile_detail.html', context)
            return redirect('/registration/profile/')
    else:
        client = Client.objects.get(user=request.user)
        form = ProfileForm(instance=client)
        context = {'form': form}
        return render(request, 'registration/profile_detail.html', context)



# def registration(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             new_user = authenticate(username=form.cleaned_data['username'],
#                                     password=form.cleaned_data['password1'],
#                                     )
#             login(request, new_user)
#             return HttpResponseRedirect("/")
#         else: 
#             print('Error')
#     else:
#         data, errors = {}, {}
#     return render(request, 'registration/reg.html',{'form': form})

@login_required(login_url='/registration/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            context = {'form': form}
            return render(request, 'registration/profile.html', context)
        else:
            return redirect('/registration/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'registration/change_password.html', context)

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/")
        else: 
            print('Error')
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registration/reg.html',{'form': form})


def index(request):
    print("index")
    return render(request, 'registration/index.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/")# Redirect to a success page.
        print("not")
    # else:
    #     form.add_error(None, 'Ошибка авторизации')
    #     return render(request, 'registration/index.html',{'login_form': form})
    return render(request, 'registration/index.html', {'login_form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

