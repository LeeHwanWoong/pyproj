# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20171204_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bdate',
            field=models.DateField(),
        ),
    ]
