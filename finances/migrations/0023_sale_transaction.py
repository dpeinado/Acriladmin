# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 02:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('finances', '0022_auto_20160629_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='transaction',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT,
                                       to='finances.Transaction', verbose_name='transacción'),
        ),
    ]
