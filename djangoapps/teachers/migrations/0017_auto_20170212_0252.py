# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0016_auto_20170212_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(max_length=50, null=True),
        ),
    ]
