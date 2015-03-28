# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150328_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('created_at',)},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 28, 21, 40, 34, 899206, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
