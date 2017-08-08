# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from .models import *


def indexHome(request):
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	# pricategoria = Categoria.objects.get(id=5, activo=True, bloqueo=True)
	# principal = Post.objects.filter(categoria=pricategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	notcategoria = Categoria.objects.get(id=1, activo=True, bloqueo=True)
	noticia = Post.objects.filter(categoria=notcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	opicategoria = Categoria.objects.get(id=4, activo=True, bloqueo=True)
	opinion = Post.objects.filter(categoria=opicategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False).order_by('-fechacreado')[:3]
	# alocategoria = Categoria.objects.get(id=3, activo=True, bloqueo=True)
	# aloido = Post.objects.filter(categoria=alocategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	# humcategoria = Categoria.objects.get(id=4, activo=True, bloqueo=True)
	# humor = Post.objects.filter(categoria=humcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	regcategoria = Categoria.objects.get(id=5, activo=True, bloqueo=True)
	region = Post.objects.filter(categoria=regcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	# intcategoria = Categoria.objects.get(id=7, activo=True, bloqueo=True)
	# internacional = Post.objects.filter(categoria=intcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	# vidcategoria = Categoria.objects.get(id=9, activo=True, bloqueo=True)
	# video = Post.objects.filter(categoria=vidcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	# entcategoria = Categoria.objects.get(id=8, activo=True, bloqueo=True)
	# entrevista = Post.objects.filter(categoria=entcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	# percategoria = Categoria.objects.get(id=5, activo=True, bloqueo=True)
	# personaje = Post.objects.filter(categoria=percategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	# ecocategoria = Categoria.objects.get(id=10, activo=True, bloqueo=True)
	# ecosbogota = Post.objects.filter(categoria=ecocategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	# teccategoria = Categoria.objects.get(id=11, activo=True, bloqueo=True)
	# tecnologia = Post.objects.filter(categoria=teccategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	ecncategoria = Categoria.objects.get(id=2, activo=True, bloqueo=True)
	economia = Post.objects.filter(categoria=ecncategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	link = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
	us = 'Home'
	context = {
		'categorias':categorias,
		# 'pricategoria':pricategoria,
		# 'principal':principal,
		'notcategoria':notcategoria,
		'noticia':noticia,
		'opicategoria':opicategoria,
		'opinion':opinion,
		# 'alocategoria':alocategoria,
		# 'aloido':aloido,
		# 'humcategoria':humcategoria,
		# 'humor':humor,
		'regcategoria':regcategoria,
		'region':region,
		# 'intcategoria':intcategoria,
		# 'internacional':internacional,
		# 'vidcategoria':vidcategoria,
		# 'video':video,
		# 'entcategoria':entcategoria,
		# 'entrevista':entrevista,
		# 'percategoria':percategoria,
		# 'personaje':personaje,
		# 'ecocategoria':ecocategoria,
		# 'ecosbogota':ecosbogota,
		# 'teccategoria':teccategoria,
		# 'tecnologia':tecnologia,
		'ecncategoria':ecncategoria,
		'economia':economia,
		'link':link,
		'us':us,
	}
	return render(request, 'home/index.html', context)


def indexAutores(request, v):
    categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
    autor = Perfil.objects.filter(activo=True, bloqueo=True, usuario__is_active=True, usuario__is_staff=False).order_by('usuario__first_name')
    link = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
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
    ws = v
    context = {
        'categorias':categorias,
        'autor':autor,
        'link':link,
        'us':us,
        'uslink':uslink,
        'vs':vs,
        'ws':ws,
    }
    return render(request, 'autor/index.html', context)


def indexAutor(request, v, w):
    categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
    autor = User.objects.get(username=v, is_active=True, is_staff=False)
#    perfil = Perfil.objects.get(usuario=autor, activo=True, bloqueo=True)
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
        'categorias':categorias,
        'autor':autor,
        'link':link,
#        'perfil':perfil,
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


def indexPost_crear(request):
    cat = Categoria.objects.filter(activo=True, bloqueo=True).order_by('titulo')
    us = 'Home'
    uslink = '/'
    vs = 'Crear post'
    context = {
        'cat':cat,
        'us':us,
        'uslink':uslink,
        'vs':vs,
    }
    return render(request, 'post/post_crear.html', context)


def indexPost(request, u, v, w):
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	acceso = Tipoacceso.objects.all()
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	post = Post.objects.get(id=v, activo=True, bloqueo=True)
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	vslink = '/' + categoria.slug + '/1/'
	ws = post.titulo
	context = {
        'categorias':categorias,
		'acceso':acceso,
		'categoria':categoria,
		'post':post,
		'link':link,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'vslink':vslink,
		'ws':ws,
	}
	return render(request, 'post/index.html', context)


def indexPost_editar(request, v, w, x):
    categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
    categoria = User.objects.get(username=v, is_active=True, is_staff=False)
    cat = Categoria.objects.filter(activo=True, bloqueo=True).order_by('titulo')
    post = Post.objects.get(id=w, activo=True, bloqueo=True)
    link = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
    us = 'Home'
    uslink = '/'
    vs = categoria.first_name + ' ' + categoria.last_name
    vslink = '/autor/' + categoria.username + '/1/'
    ws = 'Editar'
    wslink = '/backoffice/mis-post/1/'
    xs = post.titulo
    context = {
        'categorias':categorias,
        'cat':cat,
        'post':post,
        'link':link,
        'us':us,
        'uslink':uslink,
        'vs':vs,
        'vslink':vslink,
        'ws':ws,
        'wslink':wslink,
        'xs':xs,
    }
    return render(request, 'post/post_editar.html', context)


def indexCategoria(request, u, v):
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	posts = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-fechacreado')
	paginator = Paginator(posts, 10)
	try:
		page = int(v)
	except:
		page = 1
	try:
		post = paginator.page(page)
	except (EmptyPage, InvalidPage):
		post = paginator.page(paginator.num_pages)
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	ws = page
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'link':link,
		'link2':link2,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'ws':ws,
	}
	return render(request, 'categoria/index.html', context)


def indexBlog(request, v):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		posts = Post.objects.filter(activo=True, bloqueo=True).order_by('-fechacreado')
		paginator = Paginator(posts, 10)
		try:
			page = int(v)
		except:
			page = 1
		try:
			post = paginator.page(page)
		except (EmptyPage, InvalidPage):
			post = paginator.page(paginator.num_pages)
		link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
		us = 'Home'
		uslink = '/'
		vs = 'Blog'
		ws = page
		context = {
			'categorias':categorias,
			'post':post,
			'link2':link2,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'ws':ws,
		}
		return render(request, 'blog/index.html', context)
	else:
		return HttpResponseRedirect('/')


def indexCategoria(request, u, v):
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	posts = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-fechacreado')
	paginator = Paginator(posts, 10)
	try:
		page = int(v)
	except:
		page = 1
	try:
		post = paginator.page(page)
	except (EmptyPage, InvalidPage):
		post = paginator.page(paginator.num_pages)
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	ws = page
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'link':link,
		'link2':link2,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'ws':ws,
	}
	return render(request, 'categoria/index.html', context)
