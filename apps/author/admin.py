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


admin.site.register(Pais, AdminPais)
admin.site.register(Perfil, AdminPerfil)
