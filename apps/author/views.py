# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from .models import *


def indexAutores(request, v):
    try:
        autor = User.objects.filter(is_active=True, is_staff=False).order_by('first_name')
        perfil = Perfil.objects.get(usuario=autor, activo=True, bloqueo=True)
        paginator = Paginator(autor, 10)
    	try:
    		page = int(v)
    	except:
    		page = 1
    	try:
    		autor = paginator.page(page)
    	except (EmptyPage, InvalidPage):
    		autor = paginator.page(paginator.num_pages)
    	us = 'Home'
        uslink = '/'
        vs = 'Autor'
        ws = page
        context = {
            'autor':autor,
            'perfil':perfil,
            'us':us,
            'uslink':uslink,
            'vs':vs,
            'ws':ws,
        }
        return render(request, 'autor/index.html', context)
    except autor.DoesNotExist:
        raise Http404("Autor does not exist")


def indexAutor(request, v, w):
    autor = User.objects.get(username=v, is_active=True, is_staff=False)
    perfil = Perfil.objects.get(usuario=autor, activo=True, bloqueo=True)
    post = Post.objects.filter(autor=autor, activo=True, bloqueo=True)
    postcount = Post.objects.filter(autor=autor, activo=True, bloqueo=True).count()
    titulo = User.objects.get(username=v, is_active=True, is_staff=False)
    link = Post.objects.filter(autor=autor, activo=True, bloqueo=True).order_by('-vistas')[:10]
    paginator = Paginator(post, 10)
    try:
        page = int(w)
    except:
        page = 1
    try:
        post = paginator.page(page)
    except (EmptyPage, InvalidPage):
        post = paginator.page(paginator.num_pages)
    us = 'Home'
    uslink = '/'
    vs = 'Autor'
    vslink = '/autor/1/'
    ws = autor.first_name + ' ' + autor.last_name
    xs = page
    context = {
        'autor':autor,
        'link':link,
        'perfil':perfil,
        'post':post,
        'postcount':postcount,
        'titulo':titulo,
        'us':us,
        'uslink':uslink,
        'vs':vs,
        'vslink':vslink,
        'ws':ws,
        'xs':xs,
    }
    return render(request, 'autor/autor.html', context)


def indexPost(request, u, v, w):
#	if request.user.is_authenticated():
#		url = '/' + u + '/' + v + '/' + w + '/'
#		form = ComentarioForm()
#		if request.method == "POST":
#			form = ComentarioForm(request.POST)
#			if form.is_valid():
#				form.save()
#				post = form.cleaned_data['post']
#				usuario = form.cleaned_data['usuario']
#				comentario = form.cleaned_data['comentario']
#				fecha = form.cleaned_data['fecha']
#				u = Post.objects.creationform(post=post, usuario=usuario, comentario=comentario, fecha=fecha)
#				u.save()
#				return HttpResponseRedirect(url)
#			else:
#				return HttpResponseRedirect(url)

	cat = Categoria.objects.filter(menu=1)
	acceso = Tipoacceso.objects.all()
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	post = Post.objects.get(id=v, activo=True, bloqueo=True)
#	comentario = Comentario.objects.filter(post=v)[:10]
#	comentariocount = Comentario.objects.filter(post=v).count()
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
#	megustacount = Megusta.objects.filter(graf=v).count()
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	vslink = '/' + categoria.slug + '/1/'
	ws = post.titulo
	context = {
		'cat':cat,
		'acceso':acceso,
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
#		'comentario':comentario,
#		'comentariocount':comentariocount,
		'link':link,
#		'megustacount':megustacount,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'vslink':vslink,
		'ws':ws,
	}
	return render(request, 'post/index.html', context)
