# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iface', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='id_Data',
            new_name='id_data',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='module_number',
            new_name='num_reg',
        ),
        migrations.AlterField(
            model_name='data',
            name='data',
            field=models.IntegerField(null=True),
        ),
    ]