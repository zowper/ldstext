# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masstext', '0003_outboundmessage_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='recepient',
            new_name='recipient',
        ),
    ]
