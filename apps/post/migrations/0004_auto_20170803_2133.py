# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170803_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fechafinal',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='fechainicio',
            field=models.DateTimeField(blank=True),
        ),
    ]