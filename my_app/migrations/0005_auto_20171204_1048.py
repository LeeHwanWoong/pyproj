# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20171204_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dependent',
            old_name='department_name',
            new_name='dependent_name',
        ),
        migrations.AlterField(
            model_name='employee',
            name='bdate',
            field=models.DateField(),
        ),
    ]
