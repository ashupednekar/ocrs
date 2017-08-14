# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complainant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('officer_id', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
