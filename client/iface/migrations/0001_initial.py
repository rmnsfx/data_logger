# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-27 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id_Data', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.FloatField(null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('module_number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EthernetSettings',
            fields=[
                ('id_EthernetSettings', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField(null=True)),
                ('mask', models.GenericIPAddressField(null=True)),
                ('gateway', models.GenericIPAddressField(null=True)),
                ('dns', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainSettings',
            fields=[
                ('id_MainSettings', models.AutoField(primary_key=True, serialize=False)),
                ('user_login', models.CharField(max_length=50, unique=True)),
                ('user_password', models.CharField(max_length=50, null=True)),
                ('datetime', models.DateTimeField(null=True)),
                ('sync_time', models.BooleanField()),
                ('sync_server', models.URLField(null=True)),
                ('period', models.IntegerField(null=True)),
                ('remote_server', models.URLField(null=True)),
                ('change_datetime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModbusSettings',
            fields=[
                ('id_ModbusSettings', models.AutoField(primary_key=True, serialize=False)),
                ('adr_item', models.IntegerField(null=True)),
                ('type_reg', models.IntegerField(null=True)),
                ('index_reg', models.IntegerField(null=True)),
                ('type_data', models.IntegerField(null=True)),
                ('size', models.IntegerField(null=True)),
                ('multiplier', models.IntegerField(null=True)),
                ('tag', models.CharField(max_length=50, null=True)),
                ('archiving', models.BooleanField()),
                ('user_login', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='iface.MainSettings')),
            ],
        ),
        migrations.CreateModel(
            name='rs485Settings',
            fields=[
                ('id_rs485Settings', models.AutoField(primary_key=True, serialize=False)),
                ('speed', models.IntegerField(null=True)),
                ('parity', models.IntegerField(null=True)),
                ('stop_bit', models.IntegerField(null=True)),
                ('timeout', models.IntegerField(null=True)),
                ('user_login', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='iface.MainSettings')),
            ],
        ),
        migrations.AddField(
            model_name='ethernetsettings',
            name='user_login',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='iface.MainSettings'),
        ),
        migrations.AddField(
            model_name='data',
            name='user_login',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='iface.MainSettings'),
        ),
    ]
