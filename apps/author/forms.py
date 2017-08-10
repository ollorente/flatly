from django import forms

from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'categoria', 'contenido', 'acceso', 'tags', 'activo',)


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentario', 'posts',)
