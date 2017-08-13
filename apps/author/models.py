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
	fechacreado = models.DateTimeField(default=timezone.now)
	fechainicio = models.DateTimeField(default=timezone.now)
	fechamodificado = models.DateTimeField(default=timezone.now)
	acceso = models.ForeignKey(Tipoacceso, null=True, blank=True, on_delete=models.CASCADE)
	tags = models.TextField(null=True, blank=True)
	vistas = models.IntegerField(null=True, blank=True)
	activo = models.BooleanField(default=True)
	bloqueo = models.BooleanField(default=True)

	def slug(self):
		return slugify(self.titulo)

	def publish(self):
		self.fechainicio = timezone.now()
		self.save()

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
		return self.posts.titulo

	class Meta:
		ordering = ['-fecha']


class Megusta(models.Model):
	userlegusta = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	graf = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.userlegusta

	class Meta:
		ordering = ['-fecha']


class Siguiendo(models.Model):
	siguiendo = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	seguido = models.ForeignKey(Perfil)
	fecha = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.seguido.usuario.username

	class Meta:
		ordering = ['-fecha']


class Banner_categoria(models.Model):
	title = models.CharField(max_length=140)
	alias = models.SlugField(max_length=140, unique=True)

	def alias(self):
		return slugify(self.title)

	def __str__(self):
		return self.title


class Banner(models.Model):
	name = models.CharField(max_length=140)
	alias = models.SlugField(max_length=140, unique=True)
	imptotal = models.IntegerField(null=True, blank=True)
	impmade = models.IntegerField(null=True, blank=True)
	clicks = models.IntegerField(null=True, blank=True)
	clickurl = models.CharField(max_length=255, null=True, blank=True)
	state = models.BooleanField(default=False)
	catid = models.ForeignKey(Banner_categoria, null=True, blank=True, on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	custombannercode = models.TextField(max_length=2048, null=True, blank=True)
	sticky = models.BooleanField(default=False)
	ordering = models.IntegerField(default=0)
	metakey = models.TextField(null=True, blank=True)
	own_prefix = models.IntegerField(null=True, blank=True)
	add_image = models.CharField(max_length=255, null=True, blank=True)
	purchase_type = models.IntegerField(null=True, blank=True)
	track_clicks = models.IntegerField(null=True, blank=True)
	track_impressions = models.TextField(null=True, blank=True)
	checked_out = models.BooleanField(default=False)
	checked_out_time = models.DateTimeField(auto_now_add=True, blank=True)
	publish_up = models.DateTimeField(auto_now_add=True, blank=True)
	publish_down = models.DateTimeField(auto_now_add=True, blank=True)
	reset = models.DateTimeField(auto_now_add=True, blank=True)
	created = models.DateTimeField(default=timezone.now)
	modified = models.DateTimeField(auto_now_add=True, blank=True)
	modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	version = models.IntegerField(null=True, blank=True)

	def alias(self):
		return slugify(self.name)

	def __str__(self):
		return self.name


class Banner_track(models.Model):
	track_date = models.DateTimeField(default=timezone.now)
	track_type = models.IntegerField(default=0)
	banner_id = models.ForeignKey(Banner, null=True, blank=True, on_delete=models.CASCADE)
	count = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.banner_id.name
