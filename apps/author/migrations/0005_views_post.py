# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_auto_20170812_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Views_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.Post')),
            ],
        ),
    ]