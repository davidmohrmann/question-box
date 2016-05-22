# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stacked', '0012_auto_20160522_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 22, 15, 8, 11, 280873, tzinfo=utc)),
        ),
    ]
