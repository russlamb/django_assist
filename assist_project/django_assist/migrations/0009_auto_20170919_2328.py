# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_assist', '0008_auto_20170919_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='status',
            field=models.ForeignKey(default='Not Started', on_delete=django.db.models.deletion.CASCADE, to='django_assist.StepStatus'),
        ),
    ]
