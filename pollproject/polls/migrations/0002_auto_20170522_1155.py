# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_count', models.PositiveIntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Candidate')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
