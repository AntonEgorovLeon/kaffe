# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models
from ClientApp.models import Client

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Имя пользователя или пароль введены неверно!")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    agree = forms.BooleanField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'agree'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )


class ProfileForm(forms.ModelForm):
    SOCIAL_STATUS = (
        ('1','Школьник'),
        ('2','Студент'),
        ('3','Работающий'),
        ('4','Безработный'),
        ('0','Неизвестно')
    )
    SEX = (
        ('1','муж'),
        ('0','жен')
    )
    Social_status = forms.ChoiceField(choices=SOCIAL_STATUS)
    Sex = forms.ChoiceField(choices=SEX)

    class Meta():
        model = Client
        fields = [
            'Phone',
            'Site',
            'Social_status',
            'Sex'
        ]
    initial_fields = [        
            'Phone',
            'Site',
            'Social_status',
            'Sex'
    ]

    # def __init__(self, *args, **kwargs):
    #     self.Client = kwargs.pop('client')
    #     for key in self.initial_fields:
    #         if hasattr(self.Client, key):
    #             self.fields[k].initial = getattr(self.person, key)
    #     super(RegisterForm, self).__init__(*args, **kwargs) 

    def save(self, commit=True):
        client = super(ProfileForm, self).save(commit=False)
        client.Phone = self.cleaned_data['Phone']
        client.Site = self.cleaned_data['Site']
        client.Social_status = self.cleaned_data['Social_status']
        client.Sex = self.cleaned_data['Sex']
        if commit:
            client.save()

        return client