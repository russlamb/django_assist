# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_assist', '0014_auto_20170921_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='output_text',
            field=models.TextField(blank=True, default=''),
        ),
    ]