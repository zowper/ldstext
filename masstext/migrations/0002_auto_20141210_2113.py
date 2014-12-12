# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masstext', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cell_phone',
            field=models.BigIntegerField(),
            preserve_default=True,
        ),
    ]
