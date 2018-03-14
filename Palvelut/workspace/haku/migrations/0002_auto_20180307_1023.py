# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-07 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='radius',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='search',
            name='service',
            field=models.CharField(choices=[('restaurant', 'Restaurants'), ('bar', 'Bars'), ('store', 'Stores'), ('barber', 'Barbers')], max_length=30),
        ),
    ]
