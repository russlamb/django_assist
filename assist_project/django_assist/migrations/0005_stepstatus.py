# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_assist', '0004_auto_20170918_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=20)),
            ],
        ),
    ]
