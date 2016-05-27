# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 16:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finances', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventories', '0001_initial'),
        ('operations', '0001_initial'),
        ('back_office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repaircost',
            name='repair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operations.Repair', verbose_name='reparación'),
        ),
        migrations.AddField(
            model_name='productprice',
            name='authorized_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='autorizado por'),
        ),
        migrations.AddField(
            model_name='productprice',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventories.Product', verbose_name='producto'),
        ),
        migrations.AddField(
            model_name='orderservices',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.Order', verbose_name='orden'),
        ),
        migrations.AddField(
            model_name='orderservices',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Service', verbose_name='servicio'),
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.Order', verbose_name='orden'),
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.Product', verbose_name='producto'),
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Client', verbose_name='cliente'),
        ),
        migrations.AddField(
            model_name='order',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto'),
        ),
        migrations.AddField(
            model_name='materialcost',
            name='authorized_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='autorizado por'),
        ),
        migrations.AddField(
            model_name='materialcost',
            name='material',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventories.Material', verbose_name='material'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finances.Order', verbose_name='orden'),
        ),
    ]