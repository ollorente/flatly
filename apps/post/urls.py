# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import *


urlpatterns = [
	url(r'^$', indexCrear, name='vista_crearpost'),
]
