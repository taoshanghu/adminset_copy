# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-13 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconf', '0002_auto_20180312_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='configPath',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u8d1f\u8f7d\u5747\u8861\u914d\u7f6e\u6587\u4ef6\u8def\u5f84'),
        ),
    ]
