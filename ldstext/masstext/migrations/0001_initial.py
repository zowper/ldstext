# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32)),
                ('auto_admin', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InboundMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('preferred_first_name', models.CharField(max_length=16)),
                ('given_names', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('cell_phone', models.IntegerField()),
                ('verified_number', models.BooleanField(default=False)),
                ('requested_stop', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=32)),
                ('login_code', models.IntegerField()),
                ('login_code_time', models.DateTimeField()),
                ('calling', models.ForeignKey(to='masstext.Calling')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OutboundMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=16)),
                ('unit_number', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('starred', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
                ('recepient', models.ForeignKey(to='masstext.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=16)),
                ('unit_number', models.IntegerField(default=0)),
                ('stake', models.ForeignKey(to='masstext.Stake')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='outboundmessage',
            name='thread',
            field=models.ForeignKey(to='masstext.Thread'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='ward',
            field=models.ForeignKey(to='masstext.Ward'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inboundmessage',
            name='thread',
            field=models.ForeignKey(to='masstext.Thread'),
            preserve_default=True,
        ),
    ]
