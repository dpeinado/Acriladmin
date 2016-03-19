# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 03:59
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
import geoposition.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventories', '0001_initial'),
        ('back_office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='nombre')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='descripción')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='fecha de inicio')),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='fecha de finalización')),
                ('has_been_paid', models.BooleanField(default=False, verbose_name='fue cobrado')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='costo')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_office.Client', verbose_name='cliente')),
                ('sales_agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects_as_sales_agent', to='back_office.Employee', verbose_name='agente de ventas')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_supervised', to='back_office.Employee', verbose_name='supervisor')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventories.DurableGoodDefinition', verbose_name='vehículo utilizado')),
            ],
            options={
                'verbose_name_plural': 'proyectos',
                'verbose_name': 'proyecto',
            },
        ),
        migrations.CreateModel(
            name='ProjectEstimation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_office.Employee')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operations.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEstimationMaterialsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.MaterialDefinition')),
                ('project_estimation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.ProjectEstimation')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEstimationProductsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.ProductDefinition')),
                ('project_estimation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.ProjectEstimation')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMaterialsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='cantidad')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.MaterialDefinition', verbose_name='material')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto')),
            ],
            options={
                'verbose_name_plural': 'materiales',
                'verbose_name': 'material',
            },
        ),
        migrations.CreateModel(
            name='ProjectProductsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='cantidad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.ProductDefinition', verbose_name='producto')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto')),
            ],
            options={
                'verbose_name_plural': 'productos',
                'verbose_name': 'producto',
            },
        ),
        migrations.CreateModel(
            name='ProjectVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, verbose_name='observaciones')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='fecha y hora')),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='localización')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee', verbose_name='empleado')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto')),
            ],
            options={
                'verbose_name_plural': 'visitas a proyecto',
                'verbose_name': 'visita a proyecto',
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.TextField(max_length=300)),
                ('authorized_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authorized_repairs', to='back_office.Employee')),
                ('durable_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.DurableGoodDefinition')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requested_repairs', to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalesVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='localización')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Address', verbose_name='dirección')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Client', verbose_name='cliente')),
                ('sales_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_office.Employee', verbose_name='agente de ventas')),
            ],
            options={
                'verbose_name_plural': 'visitas de ventas',
                'verbose_name': 'visita de ventas',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
