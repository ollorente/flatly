# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170803_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fechamodificado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
