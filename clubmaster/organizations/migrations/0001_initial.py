# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('identifier', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('website', models.URLField(blank=True)),
                ('contact', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=140)),
            ],
        ),
    ]
