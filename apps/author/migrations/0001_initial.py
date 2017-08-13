# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 01:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('slug', models.SlugField(max_length=140)),
                ('menu', models.IntegerField(default=1)),
                ('activo', models.BooleanField(default=True)),
                ('bloqueo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=255)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Megusta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=3)),
                ('indicativo', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(max_length=20)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.TextField(blank=True, max_length=300, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('web', models.URLField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('google', models.CharField(blank=True, max_length=255, null=True)),
                ('pinterest', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('blogger', models.CharField(blank=True, max_length=255, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('bloqueo', models.BooleanField(default=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.Pais')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('contenido', models.TextField()),
                ('fechacreado', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechainicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodificado', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', models.TextField(blank=True, null=True)),
                ('vistas', models.IntegerField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('bloqueo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-fechacreado'],
            },
        ),
        migrations.CreateModel(
            name='Siguiendo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('seguido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.Perfil')),
                ('siguiendo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Tipoacceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['tipo'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='acceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Tipoacceso'),
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Categoria'),
        ),
        migrations.AddField(
            model_name='megusta',
            name='graf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Post'),
        ),
        migrations.AddField(
            model_name='megusta',
            name='userlegusta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Post'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categoria',
            name='acceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Tipoacceso'),
        ),
    ]
