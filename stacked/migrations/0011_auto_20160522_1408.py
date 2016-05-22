# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 14:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stacked', '0010_auto_20160522_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='created_date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 22, 14, 8, 7, 417561, tzinfo=utc)),
        ),
    ]
