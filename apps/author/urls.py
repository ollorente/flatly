# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import *


urlpatterns = [
    url(r'^$', indexHome, name='vista_home'),
    url(r'^buscar/(?P<v>\d+)/', search, name='vista_buscar'),
    url(r'^configuracion/$', indexPost_crear, name='vista_configuracion'),
    url(r'^rss/$', indexPost_crear, name='vista_rss'),
    url(r'^api/$', indexPost_crear, name='vista_api'),
    url(r'^soporte/$', indexPost_crear, name='vista_soporte'),
    url(r'^crear-post/$', indexPost_crear, name='vista_post_crear'),
    url(r'^autor/(?P<v>\d+)/$', indexAutores, name='vista_autores'),
    url(r'^autor/(?P<v>[\w-]+)/(?P<w>\d+)/$', indexAutor, name='vista_autor'),
    url(r'^blog/(?P<v>\d+)/$', indexBlog, name='vista_blog'),
    url(r'^editar/(?P<v>[\w-]+)/(?P<w>\d+)/(?P<x>[\w-]+)/$', indexPost_editar, name="vista_post_editar"),
    url(r'^(?P<u>[\w-]+)/(?P<v>\d+)/$', indexCategoria, name='vista_categoria'),
    url(r'^(?P<u>[\w-]+)/(?P<v>\d+)/(?P<w>[\w-]+)/$', indexPost, name="vista_post"),
    url(r'^login/$', indexLogin, name="vista_login"),
    url(r'^logout/$', indexLogout, name='vista_logout'),
	url(r'^registro/$', indexRegister, name='vista_registro'),
    url(r'^backoffice/$', indexBackoffice, name='vista_backoffice'),
    url(r'^backoffice/mis-post/(?P<w>\d+)/$', indexMis_post, name='vista_mis-post'),
    url(r'^backoffice/comentarios/(?P<w>\d+)/$', indexComentarios, name='vista_comentarios'),
    url(r'^backoffice/mis-seguidores/(?P<w>\d+)/$', indexMis_seguidores, name='vista_mis-seguidores'),
    url(r'^backoffice/los-que-sigo/(?P<w>\d+)/$', indexLos_que_sigo, name='vista_los-que-sigo'),
]
