# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-30 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20170429_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]
