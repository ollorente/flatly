# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


class Pais(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=3)
	indicativo = models.IntegerField(null=True, blank=True)
	link = models.CharField(max_length=20)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']


class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	ciudad = models.CharField(max_length=100, null=True, blank=True)
	estado = models.CharField(max_length=100, null=True, blank=True)
	pais = models.ForeignKey(Pais)
	direccion = models.TextField(max_length=300, null=True, blank=True)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)
	web = models.URLField(null=True, blank=True)
	facebook = models.CharField(max_length=255, null=True, blank=True)
	twitter = models.CharField(max_length=255, null=True, blank=True)
	youtube = models.CharField(max_length=255, null=True, blank=True)
	linkedin = models.CharField(max_length=255, null=True, blank=True)
	google = models.CharField(max_length=255, null=True, blank=True)
	pinterest = models.CharField(max_length=255, null=True, blank=True)
	instagram = models.CharField(max_length=255, null=True, blank=True)
	blogger = models.CharField(max_length=255, null=True, blank=True)
	activo = models.BooleanField(default=False)
	bloqueo = models.BooleanField(default=True)

	def __str__(self):
		return self.usuario.username

	class Meta:
		ordering = ['usuario']


class Tipoacceso(models.Model):
	tipo = models.CharField(max_length=20)

	def __str__(self):
		return self.tipo

	class Meta:
		ordering = ['tipo']


class Categoria(models.Model):
	titulo = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140)
	menu = models.IntegerField(default=1)
	acceso = models.ForeignKey(Tipoacceso, null=True, blank=True, on_delete=models.CASCADE)
	activo = models.BooleanField(default=True)
	bloqueo = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['titulo']


class Post(models.Model):
	titulo = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140, unique=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	contenido = models.TextField()
	autor = models.ForeignKey(User)
	fechacreado = models.DateTimeField(auto_now_add=True, auto_now=False)
	fechainicio = models.DateTimeField(auto_now_add=False, auto_now=True)
	fechafinal = models.DateTimeField(auto_now_add=False, auto_now=False)
	fechamodificado = models.DateTimeField(auto_now_add=False, auto_now=True)
	acceso = models.ForeignKey(Tipoacceso, null=True, blank=True, on_delete=models.CASCADE)
	tags = models.TextField(null=True, blank=True)
	vistas = models.IntegerField(null=True, blank=True)
	activo = models.BooleanField(default=True)
	bloqueo = models.BooleanField(default=True)

	def slug(self):
		return slugify(self.titulo)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['-fechacreado']


class Comentario(models.Model):
	posts = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey('auth.User')
	comentario = models.TextField(max_length=255)
	fecha = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.posts

	class Meta:
		ordering = ['-fecha']
