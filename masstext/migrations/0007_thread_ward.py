# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masstext', '0006_member_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='ward',
            field=models.ForeignKey(default=1, to='masstext.Ward'),
            preserve_default=False,
        ),
    ]
