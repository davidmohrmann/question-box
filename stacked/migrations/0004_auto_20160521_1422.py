# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 14:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stacked', '0003_auto_20160521_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 21, 14, 22, 19, 564434, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 21, 14, 22, 19, 544389, tzinfo=utc)),
        ),
    ]