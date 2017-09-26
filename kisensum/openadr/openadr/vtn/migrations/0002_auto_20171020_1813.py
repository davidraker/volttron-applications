# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 18:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drevent',
            name='last_status_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 18, 13, 4, 662688, tzinfo=utc), verbose_name='Last Status Time'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_opt_in',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 18, 13, 4, 663594, tzinfo=utc), verbose_name='Last opt-in'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_status_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 18, 13, 4, 663550, tzinfo=utc), verbose_name='Last Status Time'),
        ),
    ]
