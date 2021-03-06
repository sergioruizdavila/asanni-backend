# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-20 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='school',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='school',
            name='facebook_group',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Group on Facebook'),
        ),
        migrations.AlterField(
            model_name='school',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='school',
            name='meetup_group',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Group on Meetup.com'),
        ),
        migrations.AlterField(
            model_name='school',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='school',
            name='website',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Website'),
        ),
    ]
