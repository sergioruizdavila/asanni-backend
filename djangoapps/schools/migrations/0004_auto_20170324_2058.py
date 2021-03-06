# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_accommodationoption_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexchangeoption',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Accommodation'), (2, 'Discount in classes'), (3, 'Breakfast'), (4, 'Lunch'), (5, 'Dinner')], default=1, verbose_name='Work Exchange Categories'),
        ),
    ]
