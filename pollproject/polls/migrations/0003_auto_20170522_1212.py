# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170522_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='vote_count',
        ),
        migrations.AddField(
            model_name='candidate',
            name='vote_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
