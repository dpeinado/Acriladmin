# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_sale_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha de venta'),
        ),
    ]