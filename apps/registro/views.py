# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .forms import RegisterForm


def indexRegister(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		form = RegisterForm()
		if request.method == "POST":
			form = RegisterForm(request.POST)
			if form.is_valid():
				usuario = form.cleaned_data['username']
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				email = form.cleaned_data['email']
				password_one = form.cleaned_data['password_one']
				password_two = form.cleaned_data['password_two']
				u = User.objects.create_user(username=usuario, first_name=first_name, last_name=last_name, email=email, password=password_one)
				u.save()
				us = 'Home'
				uslink = '/'
				vs = 'Registro'
				context = {
					'us':us,
					'uslink':uslink,
					'vs':vs,
				}
				return render(request, 'registro/thanks_register.html', context)
			else:
				us = 'Home'
				uslink = '/'
				vs = 'Registro'
				context = {
					'us':us,
					'uslink':uslink,
					'vs':vs,
					'form':form,
				}
				return render(request, 'registro/index.html', context)
		us = 'Home'
		uslink = '/'
		vs = 'Registro'
		context = {
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'form':form,
		}
		return render(request, 'registro/index.html', context)
