# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=140)),
                ('organization', models.ForeignKey(to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.IntegerField(blank=True)),
                ('college', models.CharField(max_length=10)),
                ('grad_year', models.IntegerField(max_length=4)),
                ('organization', models.ForeignKey(to='organizations.Organization')),
            ],
        ),
    ]
