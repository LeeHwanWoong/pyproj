# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20171204_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bdate',
            field=models.CharField(max_length=20),
        ),
    ]
