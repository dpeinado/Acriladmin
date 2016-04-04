# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0006_remove_repair_authorized_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='fecha efectuada'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='reason',
            field=models.TextField(blank=True, max_length=300, verbose_name='motivo'),
        ),
    ]
