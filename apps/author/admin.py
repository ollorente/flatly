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


class AdminComentario(admin.ModelAdmin):
    list_display = ["fecha", "__str__", "usuario", "pk"]
    model = Comentario


class AdminMegusta(admin.ModelAdmin):
    list_display = ["fecha", "__str__", "graf", "pk"]
    model = Megusta


class AdminSiguiendo(admin.ModelAdmin):
    list_display = ["siguiendo", "__str__", "fecha", "pk"]
    model = Siguiendo


class AdminBanner_categoria(admin.ModelAdmin):
    list_display = ["__str__", "pk"]
    model = Banner_categoria


class AdminBanner(admin.ModelAdmin):
    list_display = ["__str__", "imptotal", "clicks", "created", "catid", "pk"]
    model = Banner


class AdminBanner_track(admin.ModelAdmin):
    list_display = ["__str__", "track_date", "track_type", "count", "pk"]
    model = Banner_track


admin.site.register(Pais, AdminPais)
admin.site.register(Perfil, AdminPerfil)
admin.site.register(Tipoacceso, AdminTipoacceso)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Post, AdminPost)
admin.site.register(Comentario, AdminComentario)
admin.site.register(Megusta, AdminMegusta)
admin.site.register(Siguiendo, AdminSiguiendo)
admin.site.register(Banner_categoria, AdminBanner_categoria)
admin.site.register(Banner, AdminBanner)
admin.site.register(Banner_track, AdminBanner_track)
