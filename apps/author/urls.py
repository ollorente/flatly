# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import *


urlpatterns = [
    url(r'^$', indexHome, name='vista_home'),
    url(r'^configuracion/$', indexPost_crear, name='vista_configuracion'),
    url(r'^crear-post/$', indexPost_crear, name='vista_post_crear'),
    url(r'^autor/(?P<v>\d+)/$', indexAutores, name='vista_autores'),
    url(r'^autor/(?P<v>[\w-]+)/(?P<w>\d+)/$', indexAutor, name='vista_autor'),
    url(r'^blog/(?P<v>\d+)/$', indexBlog, name='vista_blog'),
    url(r'^editar/(?P<v>[\w-]+)/(?P<w>\d+)/(?P<x>[\w-]+)/$', indexPost_editar, name="vista_post_editar"),
    url(r'^(?P<u>[\w-]+)/(?P<v>\d+)/$', indexCategoria, name='vista_categoria'),
    url(r'^(?P<u>[\w-]+)/(?P<v>\d+)/(?P<w>[\w-]+)/$', indexPost, name="vista_post"),
]
