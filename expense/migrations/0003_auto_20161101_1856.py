# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20161031_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]