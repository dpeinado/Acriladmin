# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0006_auto_20160611_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='quantity',
        ),
    ]
