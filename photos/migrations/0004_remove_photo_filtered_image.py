# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20170215_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='filtered_image',
        ),
    ]