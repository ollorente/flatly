# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20170812_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='metakey_prefix',
            new_name='add_image',
        ),
    ]
