# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-29 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170429_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='\u4f4f\u5740'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='\u59d3\u540d'),
        ),
    ]