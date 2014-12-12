# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('masstext', '0004_auto_20141211_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='newest_message_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 13, 31, 52, 819272, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calling',
            name='creation_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inboundmessage',
            name='creation_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='creation_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='outboundmessage',
            name='creation_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stake',
            name='creation_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='creation_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ward',
            name='creation_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
