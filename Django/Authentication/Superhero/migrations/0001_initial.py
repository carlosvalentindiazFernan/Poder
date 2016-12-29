# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hero',
            fields=[
                ('idhero', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('age', models.CharField(max_length=10)),
                ('power', models.CharField(max_length=40)),
            ],
        ),
    ]
