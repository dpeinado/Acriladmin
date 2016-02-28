# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 02:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interior_number', models.CharField(blank=True, max_length=5)),
                ('exterior_number', models.CharField(blank=True, max_length=5)),
                ('street', models.CharField(blank=True, max_length=20)),
                ('town', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('zip_code', models.PositiveSmallIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_since', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('number', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('seniority', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('phone', models.CharField(blank=True, max_length=14)),
                ('website', models.URLField(blank=True, max_length=45)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('picture', models.ImageField(upload_to='')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Address')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='back_office.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='PersonProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('paternal_last_name', models.CharField(max_length=20)),
                ('maternal_last_name', models.CharField(max_length=20)),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'Masculino'), (1, 'Femenino')])),
                ('phone', models.CharField(blank=True, max_length=14)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('picture', models.ImageField(upload_to='')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.Address')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.PersonProfile'),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.EmployeeRole'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.OrganizationProfile'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='administrated_branches', to='back_office.Employee'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='employees',
            field=models.ManyToManyField(to='back_office.Employee'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_office.OrganizationProfile'),
        ),
    ]
