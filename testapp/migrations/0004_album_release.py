# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20141013_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release',
            field=models.DateField(default=datetime.date(2014, 10, 14)),
            preserve_default=False,
        ),
    ]
