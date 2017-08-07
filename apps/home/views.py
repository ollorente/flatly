# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import models


def indexHome(request):
    us = 'Home'
    context = {
        'us':us,
    }
    return render(request, 'home/index.html', context)
