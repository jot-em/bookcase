# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0003_auto_20171111_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='returned_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data oddania'),
        ),
    ]
