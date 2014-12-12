# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masstext', '0005_auto_20141211_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='api_key',
            field=models.CharField(max_length=32, default='lksdflslkjsdf'),
            preserve_default=False,
        ),
    ]
