# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masstext', '0002_auto_20141210_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='outboundmessage',
            name='author',
            field=models.ForeignKey(to='masstext.Member', default=1),
            preserve_default=False,
        ),
    ]
