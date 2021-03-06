# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20171204_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT_LOCATION',
            fields=[
                ('dnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('dlocation', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='DEPF_LOCATION',
        ),
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dependent',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.RemoveField(
            model_name='works_on',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='dnumber',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dependent',
            name='essn',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='pnumber',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='works_on',
            name='essn',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
