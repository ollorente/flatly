# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from .forms import LoginForm


def indexLogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        mensaje = ""
        if request.user.is_authenticated():
            return HttpResponseRedirect('/blog/1/')
        else:
            if request.method == "POST":
                form = LoginForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    usuario = authenticate(username=username, password=password)
                    if usuario is not None and usuario.is_active:
                        login(request, usuario)
                        return HttpResponseRedirect('/blog/1/')
                    else:
                        alert = 'danger'
                        mensaje = 'Usuario y/o password incorrecto'
            form = LoginForm()
            us = 'Home'
            uslink = '/'
            vs = 'Login'
            context = {
                'us':us,
                'uslink':uslink,
                'vs':vs,
                'form':form,
                'mensaje':mensaje,
            }
            return render(request, 'home/login.html', context)


def indexLogout(request):
    logout(request)
    return HttpResponseRedirect('/')
