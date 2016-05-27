# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0006_auto_20160526_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='roles',
        ),
        migrations.AddField(
            model_name='employee',
            name='foos',
            field=models.ManyToManyField(to='back_office.EmployeeRole', verbose_name='roles'),
        ),
    ]