# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tttt_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=250, default='')),
                ('category', models.ForeignKey(to='tttt_api.Category')),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=(models.Model,),
        ),
    ]
