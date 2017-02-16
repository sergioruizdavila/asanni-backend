# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teachers', '0015_auto_20170207_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='about',
            field=models.TextField(blank=True, default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='avatar',
            field=models.TextField(blank=True, default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='born',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='methodology',
            field=models.TextField(blank=True, default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_since',
            field=models.CharField(blank=True, default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='type',
            field=models.CharField(blank=True, choices=[('H', 'Community Tutor'), ('P', 'Professional Teacher')], default='', max_length=1),
        ),
    ]
