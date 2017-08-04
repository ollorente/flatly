from django.db import models
from django.contrib.auth.models import User


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
