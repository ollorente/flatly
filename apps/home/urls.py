# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'^$', indexHome, name="vista_home"),
]
