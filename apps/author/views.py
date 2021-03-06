# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.utils.encoding import *

from .models import *
from .forms import *


def indexHome(request):
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	# pricategoria = Categoria.objects.get(id=5, activo=True, bloqueo=True)
	# principal = Post.objects.filter(categoria=pricategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	notcategoria = Categoria.objects.get(id=1, activo=True, bloqueo=True)
	noticia = Post.objects.filter(categoria=notcategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	opicategoria = Categoria.objects.get(id=4, activo=True, bloqueo=True)
	opinion = Post.objects.filter(categoria=opicategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	alocategoria = Categoria.objects.get(id=6, activo=True, bloqueo=True)
	aloido = Post.objects.filter(categoria=alocategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	humcategoria = Categoria.objects.get(id=9, activo=True, bloqueo=True)
	humor = Post.objects.filter(categoria=humcategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	regcategoria = Categoria.objects.get(id=5, activo=True, bloqueo=True)
	region = Post.objects.filter(categoria=regcategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	intcategoria = Categoria.objects.get(id=7, activo=True, bloqueo=True)
	internacional = Post.objects.filter(categoria=intcategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	vidcategoria = Categoria.objects.get(id=12, activo=True, bloqueo=True)
	video = Post.objects.filter(categoria=vidcategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	entcategoria = Categoria.objects.get(id=11, activo=True, bloqueo=True)
	entrevista = Post.objects.filter(categoria=entcategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	percategoria = Categoria.objects.get(id=10, activo=True, bloqueo=True)
	personaje = Post.objects.filter(categoria=percategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	ecocategoria = Categoria.objects.get(id=13, activo=True, bloqueo=True)
	ecosbogota = Post.objects.filter(categoria=ecocategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	teccategoria = Categoria.objects.get(id=8, activo=True, bloqueo=True)
	tecnologia = Post.objects.filter(categoria=teccategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	ecncategoria = Categoria.objects.get(id=2, activo=True, bloqueo=True)
	ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads3 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads4 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads5 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads6 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads7 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
	economia = Post.objects.filter(categoria=ecncategoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')[:3]
	link = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
	us = 'Home'
	context = {
		'categorias':categorias,
		# 'pricategoria':pricategoria,
		# 'principal':principal,
		'notcategoria':notcategoria,
		'noticia':noticia,
		'opicategoria':opicategoria,
		'opinion':opinion,
		'alocategoria':alocategoria,
		'aloido':aloido,
		'humcategoria':humcategoria,
		'humor':humor,
		'regcategoria':regcategoria,
		'region':region,
		'intcategoria':intcategoria,
		'internacional':internacional,
		'vidcategoria':vidcategoria,
		'video':video,
		'entcategoria':entcategoria,
		'entrevista':entrevista,
		'percategoria':percategoria,
		'personaje':personaje,
		'ecocategoria':ecocategoria,
		'ecosbogota':ecosbogota,
		'teccategoria':teccategoria,
		'tecnologia':tecnologia,
		'ecncategoria':ecncategoria,
		'economia':economia,
		'ads':ads,
		'ads2':ads2,
		'ads3':ads3,
		'ads4':ads4,
		'ads5':ads5,
		'ads6':ads6,
		'ads7':ads7,
		'banner':banner,
		'link':link,
		'us':us,
	}
	return render(request, 'home/index.html', context)


def indexAutores(request, v):
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	autor = Perfil.objects.filter(activo=True, bloqueo=True, usuario__is_active=True, usuario__is_staff=False).order_by('usuario__first_name')
	ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
	link = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
	# postcount = Post.objects.filter(autor__username=autor.usuario.username, fechainicio__lte=timezone.now()).count()
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
		# 'postcount':postcount,
		'ads':ads,
		'ads2':ads2,
		'banner':banner,
		'link':link,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'ws':ws,
	}
	return render(request, 'autor/index.html', context)


def indexAutor(request, v, w):
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	autor = get_object_or_404(User, username=v, is_active=True, is_staff=False)
	post = Post.objects.filter(autor=autor, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')
	postcount = Post.objects.filter(autor=autor, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).count()
	perfil = Perfil.objects.filter(usuario__username=v, activo=True, bloqueo=True)
	seguido = Siguiendo.objects.filter(seguido__usuario__username=v, siguiendo__is_active=True, siguiendo__is_staff=False).order_by('?')[:15]
	seguidocount = Siguiendo.objects.filter(seguido__usuario__username=v, siguiendo__is_active=True, siguiendo__is_staff=False).count()
	siguiendo = Siguiendo.objects.filter(siguiendo__username=v, seguido__activo=True, seguido__bloqueo=True).order_by('?')[:15]
	siguiendocount = Siguiendo.objects.filter(siguiendo__username=v, seguido__activo=True, seguido__bloqueo=True).count()
	titulo = User.objects.get(username=v, is_active=True, is_staff=False)
	ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
	link = Post.objects.filter(autor=autor, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
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
		'ads':ads,
		'ads2':ads2,
		'banner':banner,
		'link':link,
		'post':post,
		'postcount':postcount,
		'perfil':perfil,
		'seguido':seguido,
		'seguidocount':seguidocount,
		'siguiendo':siguiendo,
		'siguiendocount':siguiendocount,
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
	if request.user.is_authenticated():
		if request.method == "POST":
			form = PostForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.autor = request.user
				post.save()
				acceso = Tipoacceso.objects.filter().order_by('tipo')
				categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
				ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
				ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
				banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
				cat = Categoria.objects.filter(activo=True, bloqueo=True).order_by('titulo')
				link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
				us = 'Home'
				uslink = '/'
				vs = 'Crear post'
				context = {
					'acceso':acceso,
					'categorias':categorias,
					'ads':ads,
					'ads2':ads,
					'banner':banner,
					'cat':cat,
					'link2':link2,
					'us':us,
					'uslink':uslink,
					'vs':vs,
					'form':form,
				}
				return render(request, 'post/post_crear.html', context)
		else:
			form = PostForm()
		acceso = Tipoacceso.objects.filter().order_by('tipo')
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
		cat = Categoria.objects.filter(activo=True, bloqueo=True).order_by('titulo')
		link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
		us = 'Home'
		uslink = '/'
		vs = 'Crear post'
		context = {
			'acceso':acceso,
			'categorias':categorias,
			'ads':ads,
			'ads2':ads2,
			'banner':banner,
			'cat':cat,
			'link2':link2,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'form':form,
		}
		return render(request, 'post/post_crear.html', context)
	else:
		return HttpResponseRedirect('/')


def indexPost(request, u, v, w):
	client_ip = request.META['REMOTE_ADDR']
	if request.method == "POST":
		form = ComentarioForm(request.POST)
		if form.is_valid():
			comentario = form.save(commit=False)
			comentario.usuario = request.user
			comentario.fecha = timezone.now()
			comentario.save()
			acceso = Tipoacceso.objects.filter().order_by('tipo')
			categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
			categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
			post = get_object_or_404(Post, id=v, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now())
			comentario = Comentario.objects.filter(posts=v, usuario__is_active=True, usuario__is_staff=False)[:10]
			comentariocount = Comentario.objects.filter(posts=v, usuario__is_active=True, usuario__is_staff=False).count()
			megustacount = Megusta.objects.filter(graf=v).count()
			ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
			ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
			ads3 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
			banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
			link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
			us = 'Home'
			uslink = '/'
			vs = categoria.titulo
			vslink = '/' + categoria.slug + '/1/'
			ws = post.titulo
			context = {
				'acceso':acceso,
				'categorias':categorias,
				'categoria':categoria,
				'post':post,
				'comentario':comentario,
				'comentariocount':comentariocount,
				'megustacount':megustacount,
				'ads':ads,
				'ads2':ads2,
				'ads3':ads3,
				'banner':banner,
				'link':link,
				'us':us,
				'uslink':uslink,
				'vs':vs,
				'vslink':vslink,
				'ws':ws,
				'form': form,
				'ip':client_ip,
			}
			return render(request, 'post/index.html', context)
	else:
		form = ComentarioForm()
	acceso = Tipoacceso.objects.filter().order_by('tipo')
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	post = get_object_or_404(Post, id=v, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now())
	comentario = Comentario.objects.filter(posts=v, usuario__is_active=True, usuario__is_staff=False)[:10]
	comentariocount = Comentario.objects.filter(posts=v, usuario__is_active=True, usuario__is_staff=False).count()
	megustacount = Megusta.objects.filter(graf=v).count()
	view = Views_Post.objects.filter(post__id=v).count()
	ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads3 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	vslink = '/' + categoria.slug + '/1/'
	ws = post.titulo
	context = {
		'acceso':acceso,
		'categorias':categorias,
		'categoria':categoria,
		'post':post,
		'comentario':comentario,
		'comentariocount':comentariocount,
		'megustacount':megustacount,
		'ads':ads,
		'ads2':ads2,
		'ads3':ads3,
		'banner':banner,
		'link':link,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'vslink':vslink,
		'ws':ws,
		'form': form,
		'view':view,
	}
	return render(request, 'post/index.html', context)


def indexPost_editar(request, v, w, x):
	if request.user.is_authenticated():
		if request.user.username == v:
			post = Post.objects.get(id=w)
			if request.method == "POST":
				form = PostForm(request.POST, instance=post)
				if form.is_valid():
					post = form.save(commit=False)
					# post.autor = form.cleaned_data['fechainicio']
					post.autor = request.user
					post.save()
					acceso = Tipoacceso.objects.filter().order_by('tipo')
					categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
					categoria = User.objects.get(username=v, is_active=True, is_staff=False)
					cat = Categoria.objects.filter(activo=True, bloqueo=True).order_by('titulo')
					post = Post.objects.get(id=w, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now())
					ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
					ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
					banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
					link = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
					us = 'Home'
					uslink = '/'
					vs = categoria.first_name + ' ' + categoria.last_name
					vslink = '/autor/' + categoria.username + '/1/'
					ws = 'Editar'
					xs = w
					ys = post.titulo
					yslink = '/' + post.categoria.slug + '/' + w + '/' + x + '/'
					context = {
						'acceso':acceso,
						'categorias':categorias,
						'cat':cat,
						'post':post,
						'ads':ads,
						'ads2':ads2,
						'banner':banner,
						'link':link,
						'us':us,
						'uslink':uslink,
						'vs':vs,
						'vslink':vslink,
						'ws':ws,
						'xs':xs,
						'ys':ys,
						'yslink':yslink,
						'form': form,
					}
					return render(request, 'post/post_editar.html', context)
			else:
				form = PostForm(instance=post)
			acceso = Tipoacceso.objects.filter().order_by('tipo')
			categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
			categoria = User.objects.get(username=v, is_active=True, is_staff=False)
			cat = Categoria.objects.filter(activo=True, bloqueo=True).order_by('titulo')
			post = Post.objects.get(id=w, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now())
			ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
			ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
			banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
			link = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
			us = 'Home'
			uslink = '/'
			vs = categoria.first_name + ' ' + categoria.last_name
			vslink = '/autor/' + categoria.username + '/1/'
			ws = 'Editar'
			xs = w
			ys = post.titulo
			yslink = '/' + post.categoria.slug + '/' + w + '/' + x + '/'
			context = {
				'acceso':acceso,
				'categorias':categorias,
				'cat':cat,
				'post':post,
				'ads':ads,
				'ads2':ads2,
				'banner':banner,
				'link':link,
				'us':us,
				'uslink':uslink,
				'vs':vs,
				'vslink':vslink,
				'ws':ws,
				'xs':xs,
				'ys':ys,
				'yslink':yslink,
				'form': form,
			}
			return render(request, 'post/post_editar.html', context)
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def indexBlog(request, v):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		seguido = Siguiendo.objects.filter(seguido__usuario__username=request.user.username, siguiendo__is_active=True, siguiendo__is_staff=False).order_by('?')[:15]
		seguidocount = Siguiendo.objects.filter(seguido__usuario__username=request.user.username, siguiendo__is_active=True, siguiendo__is_staff=False).count()
		siguiendo = Siguiendo.objects.filter(siguiendo__username=request.user.username, seguido__activo=True, seguido__bloqueo=True).order_by('?')[:15]
		siguiendocount = Siguiendo.objects.filter(siguiendo__username=request.user.username, seguido__activo=True, seguido__bloqueo=True).count()
		post = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')
		posts = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')
		paginator = Paginator(post, 10)
		try:
			page = int(v)
		except:
			page = 1
		try:
			post = paginator.page(page)
		except (EmptyPage, InvalidPage):
			post = paginator.page(paginator.num_pages)
		ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
		link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
		us = 'Home'
		uslink = '/'
		vs = 'Blog'
		ws = page
		context = {
			'categorias':categorias,
			'seguido':seguido,
			'seguidocount':seguidocount,
			'siguiendo':siguiendo,
			'siguiendocount':siguiendocount,
			'post':post,
			'ads':ads,
			'ads2':ads2,
			'banner':banner,
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
	posts = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')
	paginator = Paginator(posts, 10)
	try:
		page = int(v)
	except:
		page = 1
	try:
		post = paginator.page(page)
	except (EmptyPage, InvalidPage):
		post = paginator.page(paginator.num_pages)
	ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
	link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	ws = page
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'ads':ads,
		'ads2':ads2,
		'banner':banner,
		'link':link,
		'link2':link2,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'ws':ws,
	}
	return render(request, 'categoria/index.html', context)


def search(request, v):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(titulo__icontains=query) |
			Q(contenido__icontains=query) |
			Q(autor__first_name__icontains=query) |
			Q(autor__last_name__icontains=query)
		)
		post = Post.objects.filter(qset, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).distinct().order_by('-fechacreado')
		paginator = Paginator(post, 10)
		try:
			page = int(v)
		except:
			page = 1
		try:
			post = paginator.page(page)
		except (EmptyPage, InvalidPage):
			post = paginator.page(paginator.num_pages)
	else:
		post = []
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	ads2 = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
	banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
	link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
	us = 'Home'
	uslink = '/'
	vs = 'Buscar'
	ws = page
	xs = '() ' + query
	context = {
		'categorias':categorias,
		'ads':ads,
		'ads2':ads2,
		'banner':banner,
		'link2':link2,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'ws':ws,
		'xs':xs,
		'post':post,
		'query':query
	}
	return render(request, 'buscar/index.html', context)


def indexLogin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		mensaje = ""
		if request.user.is_authenticated():
			return HttpResponseRedirect('/blog/1/')
		else:
			categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
			link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:5]
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
				'categorias':categorias,
				'link2':link2,
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
				categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
				link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
				us = 'Home'
				uslink = '/'
				vs = 'Registro'
				context = {
					'categorias':categorias,
					'link2':link2,
					'us':us,
					'uslink':uslink,
					'vs':vs,
				}
				return render(request, 'registro/thanks_register.html', context)
			else:
				categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
				link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
				us = 'Home'
				uslink = '/'
				vs = 'Registro'
				context = {
					'categorias':categorias,
					'link2':link2,
					'us':us,
					'uslink':uslink,
					'vs':vs,
					'form':form,
				}
				return render(request, 'registro/index.html', context)
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		link2 = Post.objects.filter(activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-vistas')[:10]
		us = 'Home'
		uslink = '/'
		vs = 'Registro'
		context = {
			'categorias':categorias,
			'link2':link2,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'form':form,
		}
		return render(request, 'registro/index.html', context)


def indexBackoffice(request):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		us = 'Backoffice'
		context = {
			'categorias':categorias,
			'us':us,
		}
		return render(request, 'backoffice/index.html', context)
	else:
		return HttpResponseRedirect('/')


def indexMis_post(request, w):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		autor = request.user
		post = Post.objects.filter(autor=autor, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')
		postcount = Post.objects.filter(autor=autor, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).count()
		paginator = Paginator(post, 10)
		try:
			page = int(w)
		except:
			page = 1
		try:
			post = paginator.page(page)
		except (EmptyPage, InvalidPage):
			post = paginator.page(paginator.num_pages)
		ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
		us = 'Backoffice'
		uslink = '/backoffice/'
		vs = 'Mis post'
		ws = w
		context = {
			'categorias':categorias,
			'post':post,
			'postcount':postcount,
			'ads':ads,
			'banner':banner,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'ws':ws,
		}
		return render(request, 'backoffice/mispost.html', context)
	else:
		return HttpResponseRedirect('/')


def indexComentarios(request, w):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		autor = request.user
		# post = Post.objects.filter(autor=autor, activo=True, bloqueo=True, autor__is_active=True, autor__is_staff=False, fechainicio__lte=timezone.now()).order_by('-fechacreado')
		comentario = Comentario.objects.filter(posts__autor=autor, usuario__is_active=True, usuario__is_staff=False)
		comentariocount = Comentario.objects.filter(posts__autor=autor, usuario__is_active=True, usuario__is_staff=False).count()
		paginator = Paginator(comentario, 10)
		try:
			page = int(w)
		except:
			page = 1
		try:
			comentario = paginator.page(page)
		except (EmptyPage, InvalidPage):
			comentario = paginator.page(paginator.num_pages)
		smart_text(comentario, encoding='utf-8', strings_only=False, errors='strict')
		ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
		us = 'Backoffice'
		uslink = '/backoffice/'
		vs = 'Comentarios'
		ws = w
		context = {
			'categorias':categorias,
			'comentario':comentario,
			'comentariocount':comentariocount,
			'ads':ads,
			'banner':banner,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'ws':ws,
		}
		return render(request, 'backoffice/comentarios.html', context)
	else:
		return HttpResponseRedirect('/')


def indexMis_seguidores(request, w):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
		us = 'Backoffice'
		uslink = '/backoffice/'
		vs = 'Mis seguidores'
		context = {
			'categorias':categorias,
			'ads':ads,
			'banner':banner,
			'us':us,
			'uslink':uslink,
			'vs':vs,
		}
		return render(request, 'backoffice/index.html', context)
	else:
		return HttpResponseRedirect('/')


def indexLos_que_sigo(request, w):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		ads = Banner.objects.filter(catid=1, state=True).order_by('?')[:1]
		banner = Banner.objects.filter(catid=2, state=True).order_by('?')[:1]
		us = 'Backoffice'
		uslink = '/backoffice/'
		vs = 'Los que sigo'
		context = {
			'categorias':categorias,
			'ads':ads,
			'banner':banner,
			'us':us,
			'uslink':uslink,
			'vs':vs,
		}
		return render(request, 'backoffice/index.html', context)
	else:
		return HttpResponseRedirect('/')
