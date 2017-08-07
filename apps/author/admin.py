# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from .models import *


class AdminPais(admin.ModelAdmin):
    list_display = ["__str__", "codigo", "indicativo", "link", "activo"]
    class Meta:
        model = Pais


class AdminPerfil(admin.ModelAdmin):
    list_display = ["__str__", "ciudad", "estado", "pais", "activo", "bloqueo"]
    class Meta:
        model = Perfil


class AdminTipoacceso(admin.ModelAdmin):
    list_display = ["__str__", "pk"]
    class Meta:
        model = Tipoacceso


class AdminCategoria(admin.ModelAdmin):
    list_display = ["__str__", "menu", "acceso", "activo", "bloqueo", "pk"]
    class Meta:
        model = Categoria


class AdminPost(admin.ModelAdmin):
    list_display = ["__str__", "categoria", "autor", "fechacreado", "fechamodificado", "activo", "bloqueo", "pk"]
    class Meta:
        model = Post


admin.site.register(Tipoacceso, AdminTipoacceso)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Post, AdminPost)
admin.site.register(Pais, AdminPais)
admin.site.register(Perfil, AdminPerfil)
