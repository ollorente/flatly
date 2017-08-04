# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
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
                ('acceso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Tipoacceso')),
            ],
        ),
    ]
