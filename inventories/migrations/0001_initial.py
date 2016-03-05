# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 05:18
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('back_office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('acquisition_date', models.DateField()),
                ('authorized_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consumables_authorized', to='back_office.Employee')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumableDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=45)),
                ('model', models.CharField(max_length=45)),
                ('prefix', models.SmallIntegerField(blank=True, choices=[(0, 'N/A'), (-24, 'y'), (-21, 'z'), (-18, 'a'), (-15, 'f'), (-12, 'p'), (-9, 'n'), (-6, 'μ'), (-3, 'm'), (-2, 'c'), (-1, 'd'), (1, 'da'), (2, 'h'), (3, 'k'), (6, 'M'), (9, 'G'), (12, 'T'), (15, 'P'), (18, 'E'), (21, 'Z'), (24, 'Y')], default=0)),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'm'), (2, 'in'), (3, 'ft'), (4, 'yd'), (5, 'mi'), (6, 'g'), (7, 's'), (8, 'pz'), (9, 'l')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumableInventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('consumable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.ConsumableDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumablesInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_office.BranchOffice')),
                ('items', models.ManyToManyField(blank=True, to='inventories.ConsumableInventoryItem')),
                ('last_updater', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consumables_inventories_supervised', to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='DurableGood',
            fields=[
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('acquisition_date', models.DateField()),
                ('authorized_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='durable_goods_authorized', to='back_office.Employee')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='DurableGoodDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=45)),
                ('model', models.CharField(max_length=45)),
                ('prefix', models.SmallIntegerField(choices=[(0, 'N/A'), (-24, 'y'), (-21, 'z'), (-18, 'a'), (-15, 'f'), (-12, 'p'), (-9, 'n'), (-6, 'μ'), (-3, 'm'), (-2, 'c'), (-1, 'd'), (1, 'da'), (2, 'h'), (3, 'k'), (6, 'M'), (9, 'G'), (12, 'T'), (15, 'P'), (18, 'E'), (21, 'Z'), (24, 'Y')], default=0)),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'm'), (2, 'in'), (3, 'ft'), (4, 'yd'), (5, 'mi'), (6, 'g'), (7, 's'), (8, 'pz'), (9, 'l')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DurableGoodInventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('durable_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.DurableGoodDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='DurableGoodsInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_office.BranchOffice')),
                ('items', models.ManyToManyField(blank=True, to='inventories.DurableGoodInventoryItem')),
                ('last_updater', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='durable_goods_inventories_supervised', to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'En almacén'), (1, 'Parte de un producto'), (2, 'Devuelto'), (3, 'Destruido')])),
                ('acquisition_date', models.DateField()),
                ('authorized_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='materials_authorized', to='back_office.Employee')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=50)),
                ('image', models.FileField(blank=True, upload_to='')),
                ('color', models.CharField(max_length=10)),
                ('length', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('width', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('thickness', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('weight', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('prefix', models.SmallIntegerField(blank=True, choices=[(0, 'N/A'), (-24, 'y'), (-21, 'z'), (-18, 'a'), (-15, 'f'), (-12, 'p'), (-9, 'n'), (-6, 'μ'), (-3, 'm'), (-2, 'c'), (-1, 'd'), (1, 'da'), (2, 'h'), (3, 'k'), (6, 'M'), (9, 'G'), (12, 'T'), (15, 'P'), (18, 'E'), (21, 'Z'), (24, 'Y')], default=0)),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'm'), (2, 'in'), (3, 'ft'), (4, 'yd'), (5, 'mi'), (6, 'g'), (7, 's'), (8, 'pz'), (9, 'l')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialInventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.MaterialDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialsInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_office.BranchOffice')),
                ('items', models.ManyToManyField(blank=True, to='inventories.MaterialInventoryItem')),
                ('last_updater', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='materials_inventories_supervised', to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Creación'), (1, 'Edición'), (2, 'Eliminación'), (3, 'Transferencia')])),
                ('target', models.PositiveSmallIntegerField(choices=[(0, 'Producto'), (1, 'Material'), (2, 'Empleado'), (3, 'Consumible'), (4, 'Recurso')])),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventories.Consumable')),
                ('durable_good', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventories.DurableGood')),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventories.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'En producción'), (1, 'En almacén'), (2, 'Vendido'), (3, 'Devuelto'), (4, 'Destruido')])),
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('manufacture_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('prefix', models.SmallIntegerField(blank=True, choices=[(0, 'N/A'), (-24, 'y'), (-21, 'z'), (-18, 'a'), (-15, 'f'), (-12, 'p'), (-9, 'n'), (-6, 'μ'), (-3, 'm'), (-2, 'c'), (-1, 'd'), (1, 'da'), (2, 'h'), (3, 'k'), (6, 'M'), (9, 'G'), (12, 'T'), (15, 'P'), (18, 'E'), (21, 'Z'), (24, 'Y')], default=0)),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'm'), (2, 'in'), (3, 'ft'), (4, 'yd'), (5, 'mi'), (6, 'g'), (7, 's'), (8, 'pz'), (9, 'l')], default=0)),
                ('required_units', models.PositiveSmallIntegerField(default=1)),
                ('required_amount_per_unit', models.DecimalField(decimal_places=2, default=1.0, max_digits=5)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.MaterialDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('short_description', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('color', models.CharField(max_length=10)),
                ('length', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('width', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('thickness', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('weight', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('is_composite', models.BooleanField(default=False)),
                ('prefix', models.SmallIntegerField(blank=True, choices=[(0, 'N/A'), (-24, 'y'), (-21, 'z'), (-18, 'a'), (-15, 'f'), (-12, 'p'), (-9, 'n'), (-6, 'μ'), (-3, 'm'), (-2, 'c'), (-1, 'd'), (1, 'da'), (2, 'h'), (3, 'k'), (6, 'M'), (9, 'G'), (12, 'T'), (15, 'P'), (18, 'E'), (21, 'Z'), (24, 'Y')], default=0)),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'm'), (2, 'in'), (3, 'ft'), (4, 'yd'), (5, 'mi'), (6, 'g'), (7, 's'), (8, 'pz'), (9, 'l')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.ProductDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_office.BranchOffice')),
                ('items', models.ManyToManyField(blank=True, to='inventories.ProductInventoryItem')),
                ('last_updater', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_inventories_supervised', to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('authorization_datetime', models.DateTimeField()),
                ('authorized_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee')),
                ('product_definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.ProductDefinition')),
            ],
        ),
        migrations.AddField(
            model_name='productcomponent',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.ProductDefinition'),
        ),
        migrations.AddField(
            model_name='product',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.ProductDefinition'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacture_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventories.WorkOrder'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Employee'),
        ),
        migrations.AddField(
            model_name='movement',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventories.Product'),
        ),
        migrations.AddField(
            model_name='material',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.MaterialDefinition'),
        ),
        migrations.AddField(
            model_name='durablegood',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.DurableGoodDefinition'),
        ),
        migrations.AddField(
            model_name='consumable',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.ConsumableDefinition'),
        ),
    ]
