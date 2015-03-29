# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tttt_api', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(default='', blank=True, max_length=250)),
                ('project', models.ForeignKey(to='tttt_api.Project')),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=(models.Model,),
        ),
    ]
