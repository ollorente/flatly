from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#import apps.author
#from apps.author.models import *


class Tipoacceso(models.Model):
	tipo = models.CharField(max_length=20)

	def __str__(self):
		return self.tipo


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


# class Comentario(models.Model):
# 	post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
# 	usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
# 	comentario = models.TextField(max_length=255)
# 	fecha = models.DateTimeField(auto_now_add=True, blank=True)
#
# 	def __str__(self):
# 		return self.fecha
#
# 	class Meta:
# 		ordering = ['-fecha']
#
#
# class Megusta(models.Model):
# 	usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
# 	graf = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
# 	fecha = models.DateTimeField(auto_now_add=True, blank=True)
#
# 	def __str__(self):
# 		return self.usuario
#
# 	class Meta:
# 		ordering = ['-fecha']
