# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .forms import *


def indexCrear(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.slug = request.titulo
        	# post.fechacreado = timezone.now()
        	# post.fechamodificado = timezone.now()
        	# post.author = request.user
            # post.vistas = null
            # post.activo = False
            # post.bloqueo = True
            post.save()
            return redirect('vista_crearpost')
    else:
        form = PostForm()
        us = 'Home'
        uslink = '/'
        vs = 'Crear post'
        context = {
            'us':us,
            'uslink':uslink,
            'vs':vs,
            'form':form,
        }
    return render(request, 'post/crear.html', context)
