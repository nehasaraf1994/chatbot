# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20170322_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='desgn',
        ),
        migrations.DeleteModel(
            name='doctor',
        ),
        migrations.DeleteModel(
            name='typo',
        ),
    ]
