# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-26 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0013_auto_20170426_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='alias_school',
            field=models.CharField(default='',
                                   help_text='Example: "colombia-immersion-school-2" (name splitted by - and id)',
                                   max_length=250, unique=True, verbose_name='Alias School'),
        ),
    ]
