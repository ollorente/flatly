from django import forms
from django.contrib.auth.models import User

from .models import *

class PostForm(forms.Form):

    class Meta:
        model = Post
        fields = ('titulo', 'categoria', 'contenido', 'autor', 'fechainicio', 'fechafinal', 'tags', 'acceso', 'activo',)


class ComentarioForm(forms.Form):
	post = forms.IntegerField(widget=forms.TextInput())
	usuario = forms.IntegerField(widget=forms.TextInput())
	comentario = forms.CharField(widget=forms.TextInput())
	fecha = forms.DateTimeField(widget=forms.TextInput())
