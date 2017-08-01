# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from apps.autor.models import *
# from apps.post.models import *


def indexHome(request):
    return render(request, 'home/index.html', {})
