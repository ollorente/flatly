# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import *


urlpatterns = [
    url(r'^(?P<v>\d+)/$', indexAutores, name='vista_autores'),
	url(r'^(?P<v>[\w-]+)/(?P<w>\d+)/$', indexAutor, name='vista_autor'),
    url(r'^(?P<u>[\w-]+)/(?P<v>\d+)/(?P<w>[\w-]+)/$', indexPost, name="vista_post"),
]
