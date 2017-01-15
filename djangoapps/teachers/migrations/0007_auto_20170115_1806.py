# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-15 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='value',
        ),
        migrations.AddField(
            model_name='rating',
            name='communication_value',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='rating',
            name='methodology_value',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='rating',
            name='teaching_value',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
