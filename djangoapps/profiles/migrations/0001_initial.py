# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-24 05:23
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('native', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('learn', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('teach', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('about', models.TextField(blank=True, default='', max_length=10000)),
                ('phone_number', models.CharField(blank=True, default='', max_length=30)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=1)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('born_country', models.CharField(blank=True, max_length=2)),
                ('born_city', models.CharField(blank=True, max_length=110)),
                ('avatar', models.TextField(blank=True, default='', max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('languages', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='profiles.Language')),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='locations.Location')),
            ],
        ),
    ]