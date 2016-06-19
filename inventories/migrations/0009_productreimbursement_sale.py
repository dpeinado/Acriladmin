# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0016_remove_transaction_rejection_reason'),
        ('inventories', '0008_auto_20160619_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreimbursement',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finances.Sale', verbose_name='venta relacionada'),
        ),
    ]
