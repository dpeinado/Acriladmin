# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-21 04:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventories', '0002_auto_20161020_2349'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('back_office', '0001_initial'),
        ('finances', '0002_auto_20161020_2349'),
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
                ('sales_agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects_as_sales_agent', to=settings.AUTH_USER_MODEL, verbose_name='agente de ventas')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_supervised', to=settings.AUTH_USER_MODEL, verbose_name='supervisor')),
                ('transactions', models.ManyToManyField(to='finances.Transaction', verbose_name='transacciones')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventories.DurableGood', verbose_name='vehículo utilizado')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
            },
        ),
        migrations.CreateModel(
            name='ProjectEstimation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='costo estimado')),
                ('is_approved_by_client', models.BooleanField(default=False, verbose_name='aceptada por el cliente')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto')),
            ],
            options={
                'verbose_name': 'estimación de proyecto',
                'verbose_name_plural': 'estimaciones de proyectos',
            },
        ),
        migrations.CreateModel(
            name='ProjectEstimationMaterialsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='cantidad')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.Material', verbose_name='material')),
                ('project_estimation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.ProjectEstimation', verbose_name='estimación')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiales',
            },
        ),
        migrations.CreateModel(
            name='ProjectEstimationProductsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='cantidad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.Product', verbose_name='producto')),
                ('project_estimation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.ProjectEstimation', verbose_name='estimación')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='ProjectMaterialsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='cantidad')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.Material', verbose_name='material')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiales',
            },
        ),
        migrations.CreateModel(
            name='ProjectProductsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='cantidad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.Product', verbose_name='producto')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='ProjectVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, verbose_name='observaciones')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='fecha y hora')),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='localización')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='empleado')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Project', verbose_name='proyecto')),
            ],
            options={
                'verbose_name': 'visita a proyecto',
                'verbose_name_plural': 'visitas a proyecto',
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='fecha efectuada')),
                ('reason', models.TextField(blank=True, max_length=300, verbose_name='motivo')),
                ('durable_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.DurableGood', verbose_name='objeto')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requested_repairs', to=settings.AUTH_USER_MODEL, verbose_name='solicitada por')),
            ],
            options={
                'verbose_name': 'reparación',
                'verbose_name_plural': 'reparaciones',
            },
        ),
        migrations.CreateModel(
            name='SalesVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='localización')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Address', verbose_name='dirección')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Client', verbose_name='cliente')),
                ('sales_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='agente de ventas')),
            ],
            options={
                'verbose_name': 'visita de ventas',
                'verbose_name_plural': 'visitas de ventas',
            },
        ),
    ]
