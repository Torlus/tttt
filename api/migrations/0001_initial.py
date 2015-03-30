# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=250, default='', blank=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=250, default='', blank=True)),
                ('category', models.ForeignKey(to='api.Category', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=250, default='', blank=True)),
                ('project', models.ForeignKey(to='api.Project', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('units', models.IntegerField()),
                ('owner', models.ForeignKey(related_name='works', to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
                ('task', models.ForeignKey(to='api.Task', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=(models.Model,),
        ),
    ]
