# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_assist', '0011_remove_step_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='step_order',
            field=models.IntegerField(),
        ),
    ]