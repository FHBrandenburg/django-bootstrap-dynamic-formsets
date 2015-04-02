# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('artist', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
