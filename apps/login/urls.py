# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import *


urlpatterns = [
    url(r'^$', indexLogin, name="vista_login"),
	url(r'^logout/$', indexLogout, name='vista_logout'),
]
