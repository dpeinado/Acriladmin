# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0005_auto_20160526_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(related_name='roles', to='back_office.EmployeeRole', verbose_name='roles'),
        ),
    ]