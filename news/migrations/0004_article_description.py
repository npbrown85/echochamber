# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170227_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, default=None),
        ),
    ]
